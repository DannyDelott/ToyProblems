/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/

var largestPalindromeProduct = function(max, min) {
  var largest = 0;
  for (var i = max; i >= min; i--) {
    for (var j = max; j >= min; j--) {
      if (isPalindromicNumber(i * j)) {
        largest = (i * j > largest) ? i * j : largest;
      }
    }
  }
  return largest;
};

var isPalindromicNumber = function(n) {
  var number = n.toString().split('');
  var reversed = '';
  while (number.length > 0) {
    reversed += number.pop();
  }
  return (n === parseInt(reversed));
};
