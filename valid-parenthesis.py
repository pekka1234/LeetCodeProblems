class Solution(object):
    def isValid(self, s):
        open_list = ["[","{","("]
        close_list = ["]","}",")"]        
        stack = []

        # open parenthesis will be added to stack
        # if open parenthesis has the same closed parenthesis and there is no diferent closed parentheses between (if so, False will be returned), the open parenthesis will be removed from stack 
        for i in s:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if len(stack) > 0 and open_list[pos] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
        
        # if lenght of stack is zero and the code is still running, True will be returned, otherwise False
        if len(stack) == 0:
            return True
        else:
            return False

