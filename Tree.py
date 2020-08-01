Building a Binary search tree

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	
	def insert(self,data):
		if self.data == data:
			return False
		elif self.data > data:
			if self.left:
				return self.left.insert(data)
			else :
				self.left = Node(data)
				return True
		elif self.data < data:
			if self.right:
				return self.right.insert(data)
			else :
				self.right = Node(data)
				return True
	
	def find(self,data):
		if self.data == data:
			return True
		elif self.data > data:
			if self.left:
				return self.left.find(data)
			else :
				return False
		elif self.data < data:
			if self.right:
				return self.right.find(data)
			else :
				return False
				
	
	def preorder(self):
		if self.data:
			print(self.data)
			if self.left.data:
				self.left.preorder()
			if self.right.data:
				self.right.preorder()
		else :
			return None
			
	def postorder(self):
		if self.data:
			if self.left.data:
				self.left.postorder()
			if self.right.data:
				self.right.postorder()
			print(self.data)
		else :
			return None
	
	def inorder(self):
		if self.data:
			if self.left.data:
				self.left.inorder()
			print(self.data)
			if self.right.data:
				self.right.inorder()
		else :
			return None
	

class Tree:
	def __init__(self):
		self.root = None
	
	def insert(self,data):
		if self.root:
			return self.root.insert(data)
		else :
			self.root = Node(data)
			return True
			
	def find(self,data):
		if self.root:
			return self.root.find(data)
		else :
			return False
	
	def preorder(self):
	    print("preorder")
		self.root.preorder()
	
	def postorder(self):
	    print("postorder")
		self.root.postorder()
		
	def inorder(self):
	    print("inorder")
		self.root.inorder()
		
if __name__ == "__main__":
	bst = Tree()
	for i in range(2,100,7):
		bst.insert(i*(i+4))
		
	bst.preorder()
	bst.find(134)
	bst.postorder()
	bst.inorder()
	bst.find(12)
	
	
	
	
	
	
