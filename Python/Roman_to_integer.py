class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        num = []
        value = 0
        
        if len(s) == 1:
            return roman_to_num[s]
        
        for i in s:
            num.append(roman_to_num[i])
            
        for int in range(len(num)):
            if int < len(num)-1:
                if num[int] == 0:
                    continue
                if num[int] >= num[int+1]:
                    value += num[int]
                else:
                    value += (num[int+1] - num[int])
                    num[int+1] = 0
            else:
                if num[int] > num[int-1]:
                    value += (num[int] - num[int-1])
                else:
                    value += num[int]
            
        return value