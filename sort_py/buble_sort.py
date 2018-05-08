arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50]

def buble_sort(a):
    for i in range(len(a), 0, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    buble_sort(arr)
    print(arr)
