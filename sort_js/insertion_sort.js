var swap = require('./utils').swap;

var arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50]


function insertion_sort(a) {
    for (var i = 0; i < a.length; i++) {
        var j = i - 1,
            key = a[i];
        while (j >= 0 && key < a[j]) {
            swap(a, j, j + 1);
            j--;
        }
        a[j + 1] = key;
    }
}

(function main() {
    insertion_sort(arr);
    console.log(arr);
})();