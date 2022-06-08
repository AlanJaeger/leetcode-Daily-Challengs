class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for number in nums:
            if len(str(number)) % 2 == 1:
                continue
            else:
                counter+=1

        return counter