var utils = require('./utils');

var arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50];

function max_heapify(a, start, heapSize) {
    var max = start,
        leftChild = start * 2 + 1,
        rightChild = start * 2 + 2;

    if (leftChild < heapSize && a[leftChild] > a[max]) {
        max = leftChild;
    }

    if (rightChild < heapSize && a[rightChild] > a[max]) {
        max = rightChild;
    }

    if (max != start) {
        utils.swap(a, max, start);
        max_heapify(a, max, heapSize);
    }
}

function build_heap(a) {
    var lastParent = parseInt((a.length) / 2) - 1;
    for (var i = lastParent; i >= 0; i--) {
        max_heapify(a, i, a.length);
    }
}

function heap_sort(a) {
    build_heap(a);
    for (var i = a.length - 1; i > 0; i--) {
        utils.swap(a, 0, i);
        max_heapify(a, 0, i);
    }
}

(function main() {
    heap_sort(arr);
    console.log(arr);
})();
