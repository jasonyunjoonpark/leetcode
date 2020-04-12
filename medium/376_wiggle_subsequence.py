class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        index = 1
        check = ''
        
        for num in nums:
            diff = num[index] - num[index - 1]
            index += 1
            
            
            
    
    def check_pos_or_neg(self, num):
        if num > 0:
            return '+'
        elif num < 0:
            return '-'
        elif num == 0:
            return '0'
        
if __name__ == __main__:
    s = Solution()
    print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
