var utils = require('./utils');

var arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50];


function buble_sort(a) {
    for (var i = a.length - 1; i > 0; i--) {
        for (var j = 0; j < i; j++) {
            if (a[j] > a[j + 1]) {
                utils.swap(a, j, j + 1);
            }
        }
    }
}

(function main() {
    buble_sort(arr);
    console.log(arr);
})();