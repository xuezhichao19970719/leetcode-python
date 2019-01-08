class Solution:
    def letterCombinations(self, digits):
        def mix(str1,str2):
            for i in d[str1]:
                for j in d[str2]:
                    res.append(i + j)
            return res 
        d = {"1":"1","2" : "abc" , "3" : 'def' , "4" : "ghi" , "5" : "jkl" , "6" : "mno" ,"7":"pqrs" , "8" : "tuv" , "9" : "wxyz"}
        ult = []
        map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
            for i in digits:
               if ult == []:
                    y = d[i]
                    ult += list(y)
               else:
                    ult = mix(ult,d[i])
        return ult