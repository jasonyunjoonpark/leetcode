##################################
##    001 Two Sum               ##
##################################

class Solution(object):

  def twoSum(self, nums, target):
    
    dict = {}
    i = 0
    
    for num in nums:
      compliment = target - num
      
      if compliment in dict:
        return [ dict[compliment], i ]
      else:
        dict[num] = i
      
      i += 1
