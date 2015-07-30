# ##################################################################### #
# PROMPT:                                                               #
# Find the index of a given value in a sorted list using binary search. #
# ##################################################################### #

import math

def binarySearchList( list, value, offset):
    middle = int(math.floor(len(list) / 2))
    if(value == list[middle]):
        return middle + offset
    elif(value < list[middle]):
        return binarySearchList(list[0:middle], value, offset)
    elif(value > list[middle]):
        return binarySearchList(list[middle+1:], value, middle+1)

# BinarySearchList: [1,2,3,4,5] 2 => 1
print 'BinarySearchList:\t' + '[1,2,3,4,5] 2 => ' + str(binarySearchList([1,2,3,4,5], 2, 0))

# BinarySearchList: [-21,-11,-3,0,2] 0 => 3
print 'BinarySearchList:\t' + '[-21,-11,-3,0,2] 0 => ' + str(binarySearchList([-21,-11,-3,0,2], 0, 0))

# BinarySearchList: [-21,-11,-3,0,2,5,19,21] 19 => 6
print 'BinarySearchList:\t' + '[-21,-11,-3,0,2,5,19,21] 19 => ' + str(binarySearchList([-21,-11,-3,0,2,5,19,21], 19, 0))
