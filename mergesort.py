def merge(left, right):
	ret = []
	total = len(left) + len(right)
	while len(ret) < total:
		if left and right:
			if left[0] < right[0]:
				ret.append(left.pop(0))
			else: 
				ret.append(right.pop(0))
		if not left:
			while(right):
				ret.append(right.pop(0))
		if not right:
			while(left):
				ret.append(left.pop(0))
	return ret

	
def mergesort(a):
	if len(a) > 1:
		mid = len(a)/2
		left = a[:mid]
		right = a[mid:]
		left = mergesort(left)
		right = mergesort(right)
		return merge(left, right)
	return a



if __name__ == "__main__":
	a = [1,5,6,2,3,4,9,7,8]
	a = mergesort(a)
	print a