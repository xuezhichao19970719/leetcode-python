class Solution:
    def myAtoi(self, str):
        num = "0"
        for i in str:
            if i.isdigit():
                num += i
            elif i in '+-' and num == "0":
                num = i + num
            elif i != ' ' or num != "0":
                break
        return max(min(int(num),2**31-1),-2**31)    