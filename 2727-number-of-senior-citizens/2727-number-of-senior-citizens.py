class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for deets in details:
            count += 1 if int(deets[11:13]) > 60 else 0

        return count
