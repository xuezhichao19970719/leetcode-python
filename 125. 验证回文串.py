class Solution:
    def isPalindrome(self, s):
        s = list(filter(str.isalnum,s.lower()))
        return s==s[::-1]