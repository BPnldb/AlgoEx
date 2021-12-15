
#O(nlogn)
def sortedSquaredArray(array):
    # Write your code here.
	#sortedSquares = [0 for _ in array]  #THIS WORKS TOO
    sortedSquares = [0] * len(array) # creates an array with the length x value
	print(sortedSquares)
	
	
	for i in reversed(range(len(array))): # loop through sorted array
		value = array[i]
		#print(value,"HOOO")
		sortedSquares[i] = value * value
		#print(sortedSquares[i])
	print(sortedSquares)
		
	sortedSquares.sort() #use in the case for negatives
	return sortedSquares
		
#O(n)

def sortedSquaredArray(array):
    # Write your code here.
	#sortedSquares = [0] * len(array)
	sortedSquares = [0 for _ in array]
	print(sortedSquares)
	
	leftIndex = 0
	rightIndex = len(array)-1
	
	for i in range(len(array)): #filling in the array from left to right
		if abs(array[leftIndex]) > abs(array[rightIndex]):
			sortedSquares[i] = array[leftIndex] * array[leftIndex]
			print(sortedSquares[i])
			leftIndex+=1
		else:
			sortedSquares[i] = array[rightIndex] * array[rightIndex]
			print(sortedSquares[i])
			rightIndex-=1
		print(sortedSquares)
	sortedSquares.reverse()
	return sortedSquares
