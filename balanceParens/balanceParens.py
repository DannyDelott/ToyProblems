
# #########################################################################
# PROMPT:                                                                 #
# Determine whether the parenthesis are balanced in the given expression. #
# #########################################################################

import re

def balanceParens( expression ):

    # balance parens using a stack
    parens = []
    for character in expression:

        isOpenParens = re.match('[\(\[\{]', character)
        isClosedParens = re.match('[\)\]\}]', character)

        if isOpenParens:
            parens.append(character)
        elif isClosedParens and len(parens) > 0:
            if matchParens(parens.pop()) != character:
                return False
        elif isClosedParens and len(parens) == 0:
            return False

    return len(parens) == 0

def matchParens( paren ):
    if paren == '(':
        return ')'
    elif paren == '[':
        return ']'
    elif paren == '{':
        return '}'
    elif paren == ')':
        return '('
    elif paren == ']':
        return '['
    elif paren == '}':
        return '{'

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
