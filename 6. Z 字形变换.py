class Solution:
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        result = [''] * (len(s) if numRows>len(s) else numRows)
        curr_row = 0
        for i in range(len(s)):
            result[curr_row] += s[i]
            if curr_row == 0:
                go_down = 1
            elif curr_row == numRows - 1:
                go_down = -1
            curr_row += go_down
        return "".join(result)