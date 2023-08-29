class Solution:
    def bestClosingTime(self, customers: str) -> int:
        currmax = 0
        globmax = 0
        idx = 0

        for i,s in enumerate(customers):
            if s == "N":
                currmax-=1
            else:
                currmax+=1
            
            if currmax> globmax:
                globmax = currmax
                idx = i+1
        return idx

