# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
		firstParentIdx = (len(array) - 2) // 2
		for i in reversed(range(firstParentIdx + 1)):
			self.siftDown(i, len(array) - 1, array)
		return array
        

    def siftDown(self, currentIdx, targetIdx, heap):
        # Write your code here.
		childOne = currentIdx * 2 + 1
        while childOne <= targetIdx:
			childTwo = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= targetIdx else -1
			if childTwo != -1 and heap[childOne] > heap[childTwo]:
				if heap[currentIdx] > heap[childTwo]:
					self.swap(currentIdx, childTwo, heap)
					currentIdx = childTwo
					childOne = currentIdx * 2 + 1
				else:
					return	
			else:
				if heap[currentIdx] > heap[childOne]:
					self.swap(currentIdx, childOne, heap)
					currentIdx = childOne
					childOne = currentIdx * 2 + 1
				else:
					return		

    def siftUp(self, currentIdx, heap):
        # Write your code here.
		i = (currentIdx - 1) // 2
		while i <= 0:
			if heap[currentIdx] < heap[i]:
				self.swap(currentIdx, i, heap)
				currentIdx = i
				i = (currentIdx - 1) // 2
			else:
				return
        

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap) - 1, self.heap)
		removedValue = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return removedValue
		

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]
