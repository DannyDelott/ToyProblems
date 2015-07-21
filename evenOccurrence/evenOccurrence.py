
# ############################################################################
# PROMPT:                                                                    #
# Return the first number in the array that appears an even number of times. #
# ############################################################################

def evenOccurrence( array ):

  # Build a boolean dictionary of the numbers in the array and if they're even
  def reduceEvens(dictionary, number):
    dictionary[number] = not dictionary[number] if number in dictionary else False
    return dictionary
  evens = reduce(reduceEvens, array, {})

  # Reduce the dictionary to the first even value of the array
  def reducefirstEvenOccurrence(first, number):
    first = number if first == None and evens[number] == True else first
    return first
  firstEvenOccurrence = reduce(reducefirstEvenOccurrence, array, None)

  # Return the first even occurence in the array
  return firstEvenOccurrence

# First Even Occurrence: 4
print "First Even Occurrence:\t" + str(evenOccurrence([1, 2, 3, 3, 4, 4, 3, 5, 5]))

