import re
import shutil
import logging
from pathlib import Path
from typing import Tuple

IGNORE_DIR = ['leetcode', 'others', 'old']
WORKDIR = Path.cwd()
LEETCODE_DIR = WORKDIR / 'leetcode'
EXISTING_QUESTIONS = LEETCODE_DIR.glob('*')


def parse_leetcode_info(question_directory: Path) -> Tuple[bool, str]:
    """ Parse Leetcode question info from the README generated by LeetHub."""
    readme_path: Path = question_directory / 'README.md'
    if not readme_path.exists() or not readme_path.is_file():
        return False, {}

    pattern = r'^<h2><a href="https://leetcode\.com/problems/(.*)[//]+">(\d+)\. (.*)</a></h2><h3>(.*)</h3>.*'
    matched: re.Match = re.search(pattern, readme_path.read_text())
    if matched:
        tag = matched.groups()[0]
        number = matched.groups()[1].zfill(5)
        title = matched.groups()[2]
        difficulty = matched.groups()[3]

        info = {
            "tag": tag,
            "number": number,
            "title": title,
            "difficulty": difficulty
        }

        return True, info

    return False, {}


def main():
    LEETCODE_DIR.mkdir(exist_ok=True)

    # mapping from raw question name to name with number as prefix
    existing_q_mapping = {q.name.split('_')[-1]: q.name for q in EXISTING_QUESTIONS}

    for path in WORKDIR.glob('*'):
        if path.is_file():
            continue

        if path.name in IGNORE_DIR or path.name.startswith('.'):
            continue

        ok, info = parse_leetcode_info(path)
        if not ok:
            splited = path.name.split('-', 1)
            info["number"] = splited[0].zfill(5)
            info["tag"] = splited[1]

        leetcode_number = info["number"]
        leetcode_tag = info["tag"]
        dest_dir = LEETCODE_DIR / f"{leetcode_number}_{leetcode_tag}"
        if leetcode_tag in existing_q_mapping:
            for src in path.glob('*'):
                dest_file = dest_dir / src.name
                if dest_file.exists():
                    dest_file.unlink()
                src.rename(dest_file)
            shutil.rmtree(path)
            logging.info(f"Moved all files in {path} as {dest_dir}")
        else:
            path.rename(dest_dir)


if __name__ == "__main__":
    main()