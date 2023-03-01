class Solution(object):
    def isPalindrome(self, x):
        if x > 9:
            l = [int(x) for x in str(x)]
            halflen = int((len(l) / 2))
            if list(reversed(l[:halflen])) == l[-halflen:]:
                return True
        elif x >= 0:
            return True

        return False