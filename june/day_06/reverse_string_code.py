class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
    
        while left < right:
            temp_left = s[left]
            s[left] = s[right]
            s[right] = temp_left
            
            left +=1
            right -= 1