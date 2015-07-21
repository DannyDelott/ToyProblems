/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

var specialPythagoreanTriplet = function() {
  var c = 0;
  var sum = 0;

  for (var a = 0; sum !== 1000; a++) {
    for (var b = 0; sum !== 1000; b++) {

      // find c
      c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
      if (c % 1 !== 0) continue;

      // get the sum
      sum = a + b + c;

    }
  }
  console.log(a, b, c);
  return a * b * c;

};

console.log(specialPythagoreanTriplet());
