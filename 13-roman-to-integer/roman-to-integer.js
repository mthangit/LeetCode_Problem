/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {

    let romanNumerals = new Map();
    romanNumerals.set('I', 1);
    romanNumerals.set('V', 5);
    romanNumerals.set('X', 10);
    romanNumerals.set('L', 50);
    romanNumerals.set('C', 100);
    romanNumerals.set('D', 500);
    romanNumerals.set('M', 1000);
    let res = 0;
    let i = 0;
    while(i < s.length) 
    {
        let currentValue = romanNumerals.get(s[i]);
        let nextValue = romanNumerals.get(s[i+1]);
        if (currentValue < nextValue) {
            res += (nextValue - currentValue);
            i+=2;
        } else {
            res += currentValue
            i++;
        }
    }   
    return res
};