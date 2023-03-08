class Solution(object):
    def romanToInt(self, s):
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        anwser = 0
        for i in range(len(s)):
            if i > 0 and romans[s[i]] > romans[s[i - 1]]:
                anwser += romans[s[i]] - 2 * romans[s[i - 1]]
            else:
                anwser += romans[s[i]]
        return anwser
