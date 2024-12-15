class Solution:
    def judgeCircle(self, moves: str) -> bool:
        length = len(moves)
        if (len(moves) % 2) != 0:
            return False
        moves_num = {
            "R": 1,
            "L": -1,
            "U": 2,
            "D": -2
        }
        sumud = 0
        sumrl = 0
        
        for move in moves:
            val = moves_num.get(move)
            if abs(val) == 1:
                sumud += val
                continue
            sumrl += val
        return sumud == sumrl