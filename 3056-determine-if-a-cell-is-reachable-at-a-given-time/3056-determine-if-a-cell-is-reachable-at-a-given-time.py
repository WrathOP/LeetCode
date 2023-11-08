class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy:
            if t==1:
                return False
            else:
                return True
        min_time = max(abs(sx-fx),abs(sy-fy))
        return t >= min_time