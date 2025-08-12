class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ns =str()
        for i in s:
            if i.isalnum():
                ns += i

        l = 0
        r = len(ns)-1
        while l<r:
            if ns[l] != ns[r]:
                return False
            l += 1
            r -= 1
        return True
