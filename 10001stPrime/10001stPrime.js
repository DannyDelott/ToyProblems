/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
*/

var nthPrime = function(n) {

  var primeCount = 0;
  var currentPrime = 1;
  var currentNumber = 1;

  while (primeCount < n) {
    if (isPrime(currentNumber)) {
      currentPrime = currentNumber;
      primeCount++;
    }
    currentNumber = currentNumber + 2;
  }

  return currentPrime;

};

var isPrime = function(n) {
  for (var i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
};

console.log(nthPrime(10001));
