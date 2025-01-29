# Create the Trie Node itself
class TrieNode:
    def __init__(self):
        # Two arguments: Children as a dictionary, 
        # and a boolean to detect if this is the end of the trie
        self.children = {}
        self.theend = False
        
    def printTrieNode(self, prefix):
        # If the node is the end to a word, print the word. 
        if self.theend:
            print(f'Word: {prefix}')
        # Check if there are childs. If so, navigate through them too
        for char, child in self.children.items():
            child.printTrieNode(prefix + char)
        
class Trie:
    def __init__(self):
        # The trie will be initiated with a single TrieNode
        self.root = TrieNode()
        
    def insertWord(self, word):
        # Create temporary node pointing to root
        node = self.root
        # Iterate through all the letters in the word
        for char in word:
        # Detectar se a letra existe como filho. O dicionário vai ser maior para 
            if char not in node.children:
        # Se não existir, criar.
                node.children[char] = TrieNode()
            node = node.children[char]
        node.theend = True

    def printTrie(self):
        # Call printTrieNode from the root
        self.root.printTrieNode("")
    
# Random Tests
palavras = Trie()
palavras.insertWord("Rafa")
palavras.insertWord("Rodrigo")
palavras.insertWord("Rafael")
palavras.insertWord("Rafaela")
palavras.insertWord("Rogerio")
palavras.printTrie()
