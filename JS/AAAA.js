function accum(x) {
    var my_list = [];
    for (i = 0; i < x.length; i++) {
        // x[i].upper()
        my_list += x[i].repeat(i + 1) + "-"
        console.log(my_list);        
        
    }
}



accum("abcd") /* "A-Bb-Ccc-Dddd" */
// accum("RqaEzty") /* "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy" */
// accum("cwAt") /* "C-Ww-Aaa-Tttt" */