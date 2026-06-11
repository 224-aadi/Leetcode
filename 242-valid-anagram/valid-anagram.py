class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        counter_t = {}

        if len(s) != len(t):
            return False

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            counter_t[char] = counter_t.get(char, 0) + 1
        
        if counter == counter_t:
            return True
        else:
            return False


        