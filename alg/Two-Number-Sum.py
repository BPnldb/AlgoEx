def twoNumberSum(array, targetSum):
    # Write your code here.
    
# 	seen = {}
# 	for i, v in enumerate(array):
# 		remaining = targetSum - v
# 		if remaining in seen:
# 			return [remaining, v]
# 		seen[v] = 1
# 	return []

	seen = {}
	for i,v in enumerate(array):
		remaining = targetSum-v
		if remaining in seen:
			return [remaining,v]
		seen[v] = 1
		print(seen)
	print(seen)
	return []
