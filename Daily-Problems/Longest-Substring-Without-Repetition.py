class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        NUMBER_OF_CHARACTERS = 255
        length_of_string = len(s)
        max_length = 0
        prev_index = 0
        visited_already = [-1]*NUMBER_OF_CHARACTERS


        for i in range(0,length_of_string):
            #Checks whether the current letter has been visited already
            #if it does, then the prev_index will be updated to the last time
            #the letter was seen
            #Afterward, the length is updated to see whether the current index i
            #minus the previous index, is larger than the running result
            #if it is, we update it
            #At the end of it, we update the index in the character map
            prev_index = max(prev_index, visited_already[ord(s[i])] + 1)
            max_length = max(max_length, i - prev_index + 1)
            visited_already[ord(s[i])]= i
        
        return max_length
        