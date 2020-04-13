class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff not in seen:
                seen[num] = i
            else:
                return [seen[diff], i]

if __name__ == '__main__':
        s = Solution()
        print(s.twoSum([2, 7, 11, 15], 9))
