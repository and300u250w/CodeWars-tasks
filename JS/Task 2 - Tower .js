// Build Tower
// Build Tower by the following given argument:
//     number of floors(integer and always greater than 0).

// Tower block is represented as *

//     Python: return a list;
// JavaScript: returns an Array;
// C#: returns a string[];
// PHP: returns an array;
// C++: returns a vector < string > ;
// Haskell: returns a[String];
// Ruby: returns an Array;
// Have fun!

//     for example, a tower of 3 floors looks like below

// [
//     '  *  ',
//     ' *** ',
//     '*****'
// ]
// and a tower of 6 floors looks like below

// [
//     '     *     ',
//     '    ***    ',
//     '   *****   ',
//     '  *******  ',
//     ' ********* ',
//     '***********'
// ]
// Go challenge Build Tower Advanced once you have finished this: )

// FUNDAMENTALSSTRINGSBASIC LANGUAGE FEATURES



function towerBuilder(nFloors) {
    // build here
    var lineOfStars = []
    // Creating an empy array to store our result
    for (var i = 0; i < nFloors; i++) {
    lineOfStars.push(" ".repeat(nFloors-i-1) + "*"+"*".repeat(i*2) + " ".repeat(nFloors-i-1))
    
        }
        console.log(lineOfStars);
        return lineOfStars
    }


// towerBuilder(1) 
// towerBuilder(2)
towerBuilder(10)