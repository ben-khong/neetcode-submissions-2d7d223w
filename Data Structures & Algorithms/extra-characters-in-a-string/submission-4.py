class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        cache = {len(s):0}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            # skip the current character
            res = 1 + dfs(i+1)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res, dfs(j+1))
            cache[i] = res
            return res

        return dfs(0)
