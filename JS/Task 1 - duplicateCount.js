/* Count the number of Duplicates
Write a function that will return the count of distinct case -insensitive alphabetic characters and numeric digits that occur more than once in the input string.The input string can be assumed to contain only alphabets(both uppercase and lowercase) and numeric digits.

    Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice(bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice */

function duplicateCount(text) {
    //...
    var newText = text.toUpperCase(); /* Making all letter upper case to standarize the input */
    var result = 0; 
    var tempResult = []; /* Creating an empy array to store duplicates */
    for (let i = 0; i < newText.length; i++) {

        /* Find all duplicats and add them to a new array */
        if (newText.indexOf(newText[i]) != i) { 
            tempResult.push(newText[i]);
        }
    }
    /* Find uniqie letters in array and find lenghts of the array to get our result */
    result = (tempResult.filter((v, i, a) => a.indexOf(v) === i)).length;
    return result;
}

duplicateCount("abcde");
duplicateCount("aabbcde");
duplicateCount("aabBcde");
duplicateCount("Indivisibility");
duplicateCount("Indivisibilities");