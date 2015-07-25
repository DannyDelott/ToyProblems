
# #######################################################################
# PROMPT:                                                               #
# Determine whether the parenthesis are balanced in a given expression. #
# #######################################################################

import re

def balanceParens( expression ):

    parens = []
    for char in expression:

        isOpenParens = re.match('[\(\[\{]', char)
        isClosedParens = re.match('[\)\]\}]', char)

        if isOpenParens:
            parens.append(char)
        elif isClosedParens and len(parens) > 0 and compare(parens[-1], char):
            parens.pop()
        else:
            return False

    return len(parens) == 0

def compare( openParen, closeParen ):
    return re.match('\(\)|\[\]|\{\}', openParen + closeParen)

# BalanceParens:  "()"  True
print 'BalanceParens:\t' + '"()"\t' + str(balanceParens('()'))

# BalanceParens:  "[[[]{}[]]()]"  True
print 'BalanceParens:\t' + '"[[[]{}[]]()]"\t' + str(balanceParens('[[[]{}[]]()]'))

# BalanceParens:  "({}){[]}[()]"  True
print 'BalanceParens:\t' + '"({}){[]}[()]"\t' + str(balanceParens('({}){[]}[()]'))

# BalanceParens:  "("  False
print 'BalanceParens:\t' + '"("\t' + str(balanceParens('('))

# BalanceParens:  ")("  False
print 'BalanceParens:\t' + '")("\t' + str(balanceParens(')('))

# BalanceParens:  "[{]}"  False
print 'BalanceParens:\t' + '"[{]}"\t' + str(balanceParens('[{]}'))
