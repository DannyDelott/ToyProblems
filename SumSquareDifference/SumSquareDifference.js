/*
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

var sumSquareDifference = function(max) {

  // get the sum and the sum of the squares
  var sumOfSquares = 0;
  var sum = 0;
  for (var i = 1; i <= max; i++) {
    sumOfSquares += Math.pow(i, 2);
    sum += i;
  }

  // get the square of the sum
  var squareOfSum = Math.pow(sum, 2);

  // subtract square of the sum from the sum of the squares
  return squareOfSum - sumOfSquares;

};

sumSquareDifference(100);
