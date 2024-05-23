def union(arr1,arr2):
	return (set(arr1 + arr2))

test1 = [1, 2, 3, 4, 5]

test2 = [4, 5, 6, 7, 8]

result = union(test1, test2)

print("Unified set:", result)