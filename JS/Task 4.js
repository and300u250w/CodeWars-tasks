function filter_list(l) {
    // Return a new array with the strings filtered out
    var my_list = [];
    for (i = 0; i < l.length; i++) {
        if (typeof l[i] === "number") {
            my_list.push(l[i]);
        }
    }
    return my_list

}

filter_list([1, 2, 'a', 'b'])


// Good example:
function filter_list(l) {
    return l.filter(v => typeof v == "number")
}

