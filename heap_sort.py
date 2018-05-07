arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50]

def max_heapify(a, index, heap_size):
	imax = index
	ileft = index * 2 + 1
	iright = index * 2 + 2

	if ileft < heap_size and a[ileft] > a[index]:
		imax = ileft

	if iright < heap_size and a[iright] > a[imax]:
		imax = iright

	if imax != index:
		a[index], a[imax] = a[imax], a[index]
		max_heapify(a, imax, heap_size)


def build_max_heap(a):
	heap_size = len(a)
	last_parent = (heap_size - 1) // 2
	for i in range(last_parent, -1, -1):
		max_heapify(a, i, heap_size)

def heap_sort(a):
	build_max_heap(a)
	heap_size = len(a)
	for i in range(heap_size-1, 0, -1):
		a[0], a[i] = a[i], a[0]
		max_heapify(a, 0, i)


if __name__ == '__main__':
	heap_sort(arr)
	print(arr)
