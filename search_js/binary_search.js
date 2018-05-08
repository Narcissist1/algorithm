var arr = [1, 4, 7, 9, 23, 24, 33, 41, 49, 66, 78, 92, 99, 100];

function binary_search(a, start, end, val) {
    if (end - start === 1) {
        var res;
        a[start] === val ? res = start : res = undefined;
        return res;
    }
    var mid = parseInt((end + start) / 2);
    if (a[mid] > val) {
        return binary_search(a, start, mid, val);
    }
    else if (a[mid] < val) {
        return binary_search(a, mid, end, val);
    }
    else
        return mid;
}

(function main() {
    var target = 33;
    var index = binary_search(arr, 0, arr.length, target);
    console.log(index);
})();