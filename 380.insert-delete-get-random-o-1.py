#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:
    def __init__(self):
        self.ds = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.ds:
            self.ds[val] = ""
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.ds:
            self.ds.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        random_key = random.sample(self.ds.keys(), 1)[0]
        return random_key


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

