arr = [_ for _ in range(100)]


def binary_search(_list, start, end, value):
    mid = (end + start) // 2
    if end - start == 1:
        if _list[start] != value:
            return None
        else:
            return start
    if _list[mid] == value:
        return mid
    if value < _list[mid] and mid > start:
        return binary_search(_list, start, mid, value)
    elif value > _list[mid] and mid < end:
        return binary_search(_list, mid, end, value)


if __name__ == '__main__':
    index = binary_search(arr, 0, len(arr), 25)
    print(index)
