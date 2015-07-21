/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

var smallestMultiple = function(max, min) {

  var number = 1;
  var isMultiple = false;

  while (true) {

    // test if the number is a multiple of each number in the range
    for (var i = min; i <= max; i++) {
      if (number % i !== 0) {
        isMultiple = false;
        break;
      } else {
        isMultiple = true;
      }
    }

    // If the number is a multiple of the range, return it!
    if (isMultiple) {
      return number;
    }

    number++;

  }

};

smallestMultiple(20, 1);
