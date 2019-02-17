class Solution:
    def plusOne(self, digits):
        i = ''.join(map(str,digits))
        return list(map(int, str(int(i)+1)))