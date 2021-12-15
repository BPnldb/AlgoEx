# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList #set to first node in linkedlist
	while currentNode is not None: #while LL is not empty
		print(currentNode.value)
		nextDistinctNode = currentNode.next #next distinct node = current.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value: #while distnctNode is not empty and = current
			nextDistinctNode = nextDistinctNode.next #move the distinctNode to the next one.
			
		currentNode.next = nextDistinctNode
		currentNode = nextDistinctNode
		#print(currentNode.value)
	return linkedList
