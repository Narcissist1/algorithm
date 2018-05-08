function swap(arry, i, j) {
    var tmp = arry[i];
    arry[i] = arry[j];
    arry[j] = tmp;
}

module.exports = {
    swap: swap
}
