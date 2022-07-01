#brute force method (Tn=O(n^2),Sn()=O(1))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i]+nums[k]==target:
                    return i, k
#optimized (Tn()=O(n),Sn()=O(1))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mapping value:index in the dictionary
        hash_map = {}
        for i in range(len(nums)):
          tmp = target - nums[i]
          if tmp not in hash_map:
            hash_map[nums[i]] = i
          else:
            return [i, hash_map[tmp]]
