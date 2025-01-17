class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {'}':'{',']':'[',')':'('}
        for i in s:
            if i in mappings:
                top_ele = stack.pop() if stack else '#'
                if mappings[i] != top_ele:
                    return False
            else:
                stack.append(i)
        return not stack
