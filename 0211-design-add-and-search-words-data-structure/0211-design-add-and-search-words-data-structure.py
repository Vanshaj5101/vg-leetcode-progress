class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        root = self.trie

        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['.'] = '.'

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '.' in node  # word end marker

            c = word[i]

            # Case 1: normal character
            if c != '.':
                if c not in node:
                    return False
                return dfs(node[c], i + 1)

            # Case 2: wildcard '.'
            for child in node:
                if child != '.' and dfs(node[child], i + 1):
                    return True
            return False

        return dfs(self.trie, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)