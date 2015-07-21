/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/

var largestPrimeFactor = function(n) {
  var target = n;
  var found = false;
  var divisor = 2;
  var largestPrime;

  while (!found) {

    if (target % divisor === 0) {

      var quotient = target / divisor;

      if (isPrime(quotient)) {
        found = true;
        largestPrime = quotient;
      } else {
        target = quotient;
      }

    } else {
      divisor++;
    }

  }

  return largestPrime;
};

var isPrime = function(n) {
  for (var i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
};

largestPrimeFactor(600851475143);
