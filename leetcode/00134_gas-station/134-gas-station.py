class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        rest_gas = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            rest_gas += gas[i] - cost[i]

            # 如果剩餘的油量小於0
            # 表示從這點無法走完，於是start點往下移動
            if rest_gas < 0:
                start = i + 1
                rest_gas = 0

        # 不管從哪裡開始，如果全部的油量>總消耗量，那麼一定走得完
        return start if total >= 0 else -1
