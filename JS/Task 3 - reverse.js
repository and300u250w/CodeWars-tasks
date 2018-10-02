// Complete the solution so that it reverses the string value passed into it.

// solution('world'); // returns 'dlrow'

// function solution(str) {
//     var string = "";
//     for (i = 0; i < str.length; i++) {
//         string += str[(str.length - 1) - i];
//     }
//     return string
// }


function solution(str) {  
    return str.split('').reverse().join('');
}


solution('world');


