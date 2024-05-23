def find_intersection(arr1, arr2):
	intersection = []
	for num in arr1:
		if num in arr2:
			intersection.append(num)
	return intersection
test1 = [1, 2, 3, 4, 5]
test2 = [4, 5, 6, 7, 8]
result = find_intersection(test1, test2)
print("Intersection:", result)
