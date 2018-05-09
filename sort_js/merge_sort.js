var arr = [21, 75, 40, 89, 72, 2, 45, 32, 28, 7, 56, 58, 60, 64, 50];


function merge(la, lb) {
    var tmp = [];
    while (la.length > 0 || lb.length > 0) {
        if (la.length === 0) {
            tmp = tmp.concat(lb);
            return tmp;
        }
        else if (lb.length === 0) {
            tmp = tmp.concat(la);
            return tmp;
        }
        la[0] > lb[0] ? tmp.push(lb.shift()) : tmp.push(la.shift());
    }
    return tmp;
}

function divide(a) {
    if (a.length > 1) {
        var mid = parseInt(a.length / 2);
        return merge(divide(a.slice(0, mid)), divide(a.slice(mid, a.length)));
    }
    else {
        return a;
    }
}

(function main() {
    var res = divide(arr);
    console.log(res);
})();