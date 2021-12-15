# O(n) time

def isValidSubsequence(array, sequence):
	mainIndex = 0
	subIndex = 0
	
	while mainIndex < len(array) and subIndex < len(sequence):
		if array[mainIndex] == sequence[subIndex]:
			subIndex+=1
		mainIndex+=1
	return subIndex == len(sequence)


# O(n) time
def isValidSubsequence(array, sequence):
    # Write your code here.
    subIndex = 0
	
	
# 	for i in range(len(array)):
# 		if subIndex == len(sequence): # if the length = 0
# 			return True
# 		elif array[i] == sequence[subIndex]:
# 			subIndex+=1
			
# 	return subIndex == len(sequence)


	for i in array:
		if subIndex == len(sequence):
			return True
		elif i == sequence[subIndex]:
			subIndex+=1
	return subIndex == len(sequence)
