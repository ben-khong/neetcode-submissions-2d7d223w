"""
variable for prefix 
ranged based for loop 
    nested for loop to go through every string
        if statement if i == len str or the characters arent the same
            return substr 
    add the character to prefix

O(N), O(N)

strs=["a","a","a"]


"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
        
