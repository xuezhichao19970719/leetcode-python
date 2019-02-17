class Solution:
    def lengthOfLastWord(self, s):
        data = s.strip().split(' ')
        return len(data.pop())