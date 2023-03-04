class Solution(object):
    def isPalindrome(self, x):
        if x > 9:
            # number is turned to digit list
            # middle of the list is taken, rounded downwards becouse it doesn't matter if the exact middle stays unchekced
            # if the start of the list reversed is the end of the list reversed, then it is palindrome
            l = [int(x) for x in str(x)]
            halflen = int((len(l) / 2))
            if list(reversed(l[:halflen])) == l[-halflen:]:
                return True
        elif x >= 0:
            return True

        return False
