class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        jewel_map = {}
        for jewel in jewels:
            jewel_map[jewel] = True

        for stone in stones:
            if stone in jewel_map:
                res += 1
        return res