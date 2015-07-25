
# #########################################################################
# PROMPT:                                                                 #
# Determine whether the parenthesis are balanced in the given expression. #
# #########################################################################

def balanceParens( expression ):

    # balance parens using a stack
    stack = []
    for character in expression:
        if character == '(':
            stack.append('(')
        elif character == ')' and len(stack) > 0:
            stack.pop()
        else:
            return False;

    return len(stack) == 0

# BalanceParens:  "("  False
print 'BalanceParens:\t' + '"("\t' + str(balanceParens(')'))

# BalanceParens:  ")("  False
print 'BalanceParens:\t' + '")("\t' + str(balanceParens(')('))

# BalanceParens:  "()"  True
print 'BalanceParens:\t' + '"()"\t' + str(balanceParens('()'))

# BalanceParens:  "(()())"  True
print 'BalanceParens:\t' + '"(()())"\t' + str(balanceParens('(()())'))
