# ###################### #
# PROMPT:                #
# Implement bubble sort. #
# ###################### #

def bubbleSort( list ):
    hasSwapped = True
    while hasSwapped == True:
        hasSwapped = False
        for i, number in enumerate(list):
            if (i == len(list) - 1) or (list[i] < list[i+1]): continue
            list[i] = list[i+1]
            list[i+1] = number
            hasSwapped = True
    return list

# yields [1, 2, 3]
print bubbleSort([2, 1, 3])

# yields [-2, -1, 0, 1, 2, 3, 4]
print bubbleSort([2, 4, 0, -1, 1, 3, -2])
