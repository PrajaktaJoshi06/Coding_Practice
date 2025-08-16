class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = list(str(num))
        
        # Change the first '6' we encounter to '9'
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break
        
        # Convert back to integer
        return int("".join(num_str))