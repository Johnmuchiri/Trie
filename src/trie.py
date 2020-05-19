class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False
        self.score = 0


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insertNode(self, word):
        node = self.root
        for w in word:
            if w in node.children.keys():
                node = node.children[w]
            else:
                new_node = TrieNode(w)
                node.children[w] = new_node
                node = new_node
            node.isWord = True

    """
    @:param word:str
    @:return bool 
    """

    def search(self, word):

        curr = self.root

        for w in word:

            if w in curr.children.keys():
                print(w)
                curr = curr.children[w]
            else:
                return False

        return curr is not None and curr.isWord


trie = Trie()
trie.insertNode("john")
trie.insertNode("james")
trie.insertNode("judy")

print(trie.search("john"))
