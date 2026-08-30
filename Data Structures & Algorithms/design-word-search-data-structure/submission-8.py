"""
Create a prefix node class and think of word dictionary as a prefix tree. Have dictionary for children and boolean to mark the end of a word

in the word dictionary constructor initialize the root

in add word use a curr variable and for loop to traverse and if cur character does not exist create prefix node. At the end update the boolean to mark it as a word

recursive dfs function to check every path? if match return true 
"""
class PrefixNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = PrefixNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixNode()
            curr = curr.children[c]
        curr.endOfWord = True 

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)


