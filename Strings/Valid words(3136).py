class Solution(object):
    def isValid(self, word):
        alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        vowel = "aeiouAEIOU"
        contains_vowel = False
        contains_consonant = False
        if len(word) < 3 :
            return False
        for c in word:
            if c in alpha:
                if c in vowel:
                    contains_vowel = True
                else:
                    contains_consonant = True
            elif c not in digits:
                return False
        
        return contains_consonant and contains_vowel


#Time complexity : O(N)
#Space complexity : O(1)
