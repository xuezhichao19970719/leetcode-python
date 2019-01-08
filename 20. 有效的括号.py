class Solution:
    def isValid(self, s):
        opens = "([{"
        closers = ")]}"
        l = []
        for i in s:
            if i in opens:
                l.append(opens.index(i))
            elif l == [] or l.pop() - closers.index(i):
                return False
        return l == []