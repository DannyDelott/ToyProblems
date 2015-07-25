
# ######################################################################
# PROMPT:                                                              #
# Return all of the anagrams that can be formed from the input string. #
# ######################################################################

def allAnagrams( input ):

    anagrams = {}

    def subroutine( anagram, remaining ):

        # Base Case: add anagram to dictionary
        if len(anagram) == len(input):
            anagrams[anagram] = True
            return;

        # Recursive Case: continue building the anagram
        for index, character in enumerate(remaining):
            currentAnagram = anagram + character
            currentRemaining = remaining[0: index] + remaining[index+1:]
            subroutine(currentAnagram, currentRemaining)

    subroutine('', input)
    return anagrams.keys()

# All Anagrams: ['acb', 'abc', 'bca', 'cba', 'bac', 'cab']
# Total Anagrams: 6
anagrams = allAnagrams('abc')
print 'All Anagrams:\t' + str(anagrams)
print 'Total Anagrams:\t' + str(len(anagrams))
