arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50]


def partition(a, start, end):
    pivot = a[start]
    left_index = start + 1
    right_index = end
    while left_index < right_index:
        while a[left_index] < pivot and left_index < end:
            left_index += 1
        while a[right_index] > pivot and right_index > start:
            right_index -= 1
        if left_index < right_index:
            a[left_index], a[right_index] = a[right_index], a[left_index]
    if a[start] > a[right_index]:
        a[start], a[right_index] = a[right_index], a[start]
    return right_index


def quick_sort(a, start, end):
    if end - start < 1:
        return
    pivot = partition(a, start, end)
    quick_sort(a, start, pivot-1)
    quick_sort(a, pivot+1, end)


if __name__ == '__main__':
    quick_sort(arr, 0, len(arr)-1)
    print(arr)
