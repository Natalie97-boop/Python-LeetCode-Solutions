class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        temp_string_1 = ""
        temp_string_2 = ""
        
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        if len_word1 == 1 and len_word2 == 1:
            if word1[0] == word2[0]:
                return True
            else:
                return False
        
        for i in range(0,len_word1):
            temp_string_1 += word1[i]
        
        for j in range(0,len_word2):
            temp_string_2 += word2[j]
            
        if temp_string_1 == temp_string_2:
            return True
        else:
            return False
            