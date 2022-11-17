import collections


def get_minimum_connections(matrix):
    # graph = collections.defaultdict(list)
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] == True:
    #             graph[i].append(j)
    graph = {}
    for i in range(len(matrix)):
        graph[i] = []
        for j in range(len(matrix[0])):
            if matrix[i][j] == True:
                if not graph[i]:
                    graph[i] = [j]
                else:
                    graph[i].append(j)

    # BFS
    nums_of_part = 0
    queue = [] # start
    visited = [False] * len(graph)
    while not all(visited):
        queue = [visited.index(False)]
        while queue:
            curr_node = queue.pop()
            for neighbour in graph[curr_node]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    queue.append(neighbour)
        nums_of_part += 1

    return nums_of_part-1


if __name__ == "__main__":
    matrix = [
        [False, True, False, False, True],
        [True, False, False, False, False],
        [False, False, False, True, False],
        [False, False, True, False, False],
        [True, False, False, False, False]
    ]

    print(get_minimum_connections(matrix))
