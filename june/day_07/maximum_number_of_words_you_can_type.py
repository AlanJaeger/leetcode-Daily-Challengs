class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        counter = 0
        for word in text.split():
            for letter in brokenLetters:
                if letter in word:
                    break
            else:
                counter+=1
        return counter