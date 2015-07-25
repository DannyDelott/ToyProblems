
# #########################################################################
# PROMPT:                                                                 #
# Determine whether the parenthesis are balanced in the given expression. #
# #########################################################################

def balanceParens( expression ):

    # Read parens from expression into a stack (FILO)
    stack = []
    for character in expression:
        if(character == '(' or character == ')'): stack.append(character)

    # Evaluate parens from stack
    balance = []
    for character in reversed(stack):
        if character == ')': balance.append(')')
        elif character == '(' and len(balance) > 0: balance.pop()
        else: return False;

    return len(balance) == 0

# BalanceParens:  "("  False
print 'BalanceParens:\t' + '"("\t' + str(balanceParens(')'))

# BalanceParens:  ")("  False
print 'BalanceParens:\t' + '")("\t' + str(balanceParens(')('))

# BalanceParens:  "()"  True
print 'BalanceParens:\t' + '"()"\t' + str(balanceParens('()'))

# BalanceParens:  "(()())"  True
print 'BalanceParens:\t' + '"(()())"\t' + str(balanceParens('(()())'))
