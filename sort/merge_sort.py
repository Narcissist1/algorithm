arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50]


def merge(la, lb):
    tmp = []
    while la or lb:
        if not la:
            tmp.extend(lb)
            return tmp
        elif not lb:
            tmp.extend(la)
            return tmp
        if la[0] < lb[0]:
            tmp.append(la.pop(0))
        else:
            tmp.append(lb.pop(0))
    return tmp


def divide(a):
    if len(a) > 1:
        mid = len(a) // 2
        return merge(divide(a[0: mid]), divide(a[mid: len(a)]))
    else:
        return a


if __name__ == '__main__':
    res = divide(arr)
    print(res)
