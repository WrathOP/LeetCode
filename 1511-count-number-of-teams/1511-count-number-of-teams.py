class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for mid in range(1,len(rating)-1):
            #ascending case first 
            left = right = 0

            for i in range(mid):
                if rating[i] < rating[mid]:
                    left+=1
            for i in range(mid+1, len(rating)):
                if rating[i] > rating[mid]:
                    right+=1
                
            res+= left*right
            # yaha sare ascending vale case nibadgye iss mid ke
            res+= (mid-left) * (len(rating)-1 - mid - right)
            #ye gye saare descending vale
            
        return res