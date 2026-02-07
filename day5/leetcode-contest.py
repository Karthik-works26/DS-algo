class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        
        preL = [0] * (n + 2)
        preLC = [0] * (n + 2)
        
        l = 0
        lc = 0
        countLCT = 0

        for i in range(n):
            if s[i] == 'L':
                l += 1
            elif s[i] == 'C':
                lc += l
            elif s[i] == 'T':
                countLCT += lc
            preL[i + 1] = l
            preLC[i + 1] = lc
        
        sufT = [0] * (n + 5)
        sufCT = [0] * (n + 5)
        t = 0
        ct = 0

        for i in range(n - 1, -1, -1):
            if s[i] == 'T':
                t += 1
            elif s[i] == 'C':
                ct += t
            sufT[i + 1] = t
            sufCT[i + 1] = ct

        
        answer1 = sufCT[1] + countLCT
        
        
        answer2 = preLC[n] + countLCT
        
       
        answer3 = 0
        for i in range(1, n + 1):
            answer3 = max(answer3, preL[i] * sufT[i + 1])
        
        return max(answer1, answer2, answer3 + countLCT)
