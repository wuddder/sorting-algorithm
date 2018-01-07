def quicksort(left, right, a):
	if left < right:
		p = partition(left, right, a)
		quicksort(left, p, a)
		quicksort(p+1, right, a)
	return 

def partition(left, right, a):
	pivot = a[right-1]
	i = left - 1
	for j in xrange(left, right):
		if a[j] < pivot:
			i += 1
			a[i], a[j] = a[j], a[i]

	if a[right-1] < a[i+1]:
		a[right-1], a[i+1] = a[i+1], a[right-1]

	return (i + 1)


if __name__ == "__main__":
	a = [1,5,6,2,3,4,9,7]
	if not a: 
		print a 
		return 
	quicksort(0, len(a), a)
	print a
	return 
