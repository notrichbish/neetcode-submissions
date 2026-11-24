class Solution:
    def isValid(self, s: str) -> bool:
        comp_dict = {')':'(', '}':'{', ']':'['}
        stack_s = [] # for open brackets ONLY
        for i in s:
            if i not in comp_dict: # this one only compares the 'key' from the dict which consist only close brackets
                stack_s.append(i)
            elif len(stack_s) == 0 or stack_s[-1] != comp_dict[i]:
                return False 
            else:
                stack_s.pop()
        return len(stack_s) == 0