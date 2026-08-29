"""
make class for prefix node and have it contain a hashmap for its children and boolean marking the end of a word

in the constructor for prefixTree, create a root node using the prefix node class

for insertion, create a cur variable (root) and use a for loop to traverse and eventually create a new prefix node. dont forget to update the boolean to mark it as as word

for search we would use a cur variable and for loop for traversal. if the current character does not exist, return false. Eventually we would return if our pos is marked as a word because there could be a longer word with the same sequence of characters

same as search but at the end instead of returning the bool return true 
""" 
class PrefixNode:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return True
        