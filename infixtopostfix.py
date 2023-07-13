from stack import Stack


def inToPostFix(inexp):
    # Define the precedence dictionary for operators
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    # Create an empty stack to store operators
    stk = Stack()

    # Create an empty list to store the postfix expression
    output = []

    # Convert the input expression to a list of tokens
    tkl = list(inexp)

    # Iterate through each token in the token list
    for token in tkl:
        # Skip whitespace tokens
        if token == " ":
            continue

        # If the token is alphanumeric, add it to the output list
        if token.isalnum():
            output.append(token)

        # If the token is an opening parenthesis, push it onto the stack
        elif token == "(":
            stk.push(token)

        # If the token is a closing parenthesis, pop the stack until an opening parenthesis is encountered
        # and add the popped tokens to the output list
        elif token == ")":
            topToken = stk.pop()
            while topToken != "(":
                output.append(topToken)
                topToken = stk.pop()

        # If the token is an operator, pop operators from the stack and add them to the output list
        # until an operator with lower precedence is encountered
        else:
            while (not stk.isEmpty()) and (prec[stk.peek()] >= prec[token]):
                output.append(stk.pop())
            stk.push(token)

    # Pop any remaining operators from the stack and add them to the output list
    while not stk.isEmpty():
        output.append(stk.pop())

    # Convert the output list to a string and return the postfix expression
    return " ".join(output)


print(inToPostFix("( (A + B) - C * ( D / E ) ) + F "))
