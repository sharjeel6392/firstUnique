class Solution:
    def firstUniqChar(self, s: str) -> int:
        length = len(s)
        tempS = list(s)

        for i in range(length-1):
            value = tempS[i]
            if value == "-":
                continue
            for j in range(i+1,length):
                if tempS[j] == value:
                    tempS[j] = "-"
                    tempS[i] = "-"
        
        for i in range(length):
            if tempS[i] != "-":
                return i

        if i+1 == length:
            return -1
