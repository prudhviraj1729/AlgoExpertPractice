def multiStringSearch(bigString, smallStrings):
    # Write your code here.
	trie = Trie()
	for each_string in smallStrings:
		trie.insert(each_string)
	mapping = {}
	for i in range(len(bigString)):
		findSmallStrings(bigString, i, mapping, trie)
	return [each in mapping for each in smallStrings]

def findSmallStrings(string, index, mapping, trie):
	node = trie.root
	for i in range(index, len(string)):
		if string[i] not in node:
			break
		node = node[string[i]]
		if trie.endSymbol in node:
			mapping[node[trie.endSymbol]] = True
    
	
class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"
	
	def insert(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = string