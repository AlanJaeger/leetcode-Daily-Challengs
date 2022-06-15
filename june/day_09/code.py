class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative_list = []
        positive_list = []
        numbers = []
        
        # Creating the list of negatives and positives, i append all the numbers in positive to easy the IF, 
        # Making like that, i dont need to transform the number, just verify if he are negative.
        for num in nums:
            if num < 0:
                negative_list.append(num*-1)
            else:
                positive_list.append(num)

	# Now i create the list with all numbers positive. 
        for num in nums:
                if num < 0:
                    numbers.append(num*-1)
                else:
                    numbers.append(num)
	
	# Get the minimun value
        minimun_value = min(numbers)
	
	# And verify, if number are in negative only, return him transformed in negative.
        if minimun_value in negative_list:
	    # If the number are in both lists, return him positive, because are larger.
            if minimun_value in negative_list and minimun_value in positive_list:
                return(minimun_value )
            else:
                return(minimun_value*-1)
        # If the number are only in positive, just return him.
        elif men in post:
            return(minimun_value)