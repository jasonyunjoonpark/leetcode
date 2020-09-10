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

      
##################################
##    002 Add Two Numbers       ##
##################################      
class ListNode(object):
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
                       
class Solution(object):
    def addTwoNumbers(self, l1, l2):
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
