arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50]


def insertion_sort(a):
    for i in range(len(a)):
        j = i - 1
        key = a[i]
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key


if __name__ == '__main__':
    insertion_sort(arr)
    print(arr)
