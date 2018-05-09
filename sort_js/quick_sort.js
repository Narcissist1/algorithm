var swap = require('./utils').swap;
var arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50];


function partition(a, start, end) {
    var
        pivot = a[start],
        left_index = start + 1,
        right_index = end;
    while (left_index < right_index) {
        while (a[left_index] < pivot && left_index < end) {
            left_index++;
        }
        while (a[right_index] > pivot && right_index > start) {
            right_index--;
        }
        if (left_index < right_index) {
            swap(a, left_index, right_index);
        }
    }
    if (a[right_index] < pivot) {
        swap(a, start, right_index);
    }
    return right_index;
}

function quick_sort(a, start, end) {
    if (end - start < 1) {
        return;
    }
    var pivot_index = partition(a, start, end);
    quick_sort(a, start, pivot_index - 1);
    quick_sort(a, pivot_index + 1, end);
}

(function main() {
    quick_sort(arr, 0, arr.length - 1);
    console.log(arr);
})();