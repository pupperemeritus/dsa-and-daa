from stack import Stack


def pFEval(pfExp):
    """
    Evaluates the given postfix expression and returns the result.

    Args:
        pfExp (str): The postfix expression to be evaluated.

    Returns:
        float: The result of the postfix expression evaluation.
    """
    operand = Stack(100)  # Create a stack to store operands
    tokenlist = pfExp.split()  # Split the postfix expression into tokens

    for token in tokenlist:
        if token.isalnum():  # If token is alphanumeric, it is an operand
            operand.push(float(token))  # Push the operand to the stack
        else:
            operand2 = operand.pop()  # Pop the top operand from the stack
            operand1 = operand.pop()  # Pop the second top operand from the stack
            result = doMath(token, operand1, operand2)  # Perform the operation
            operand.push(result)  # Push the result back to the stack

    return operand.pop()  # Return the final result


def do_math(op: str, op1: float, op2: float) -> float:
    """
    Perform basic arithmetic operations on two numbers.

    Args:
        op (str): The operation to be performed. Valid values are "*", "/", "+", and "-".
        op1 (float): The first operand.
        op2 (float): The second operand.

    Returns:
        float: The result of the arithmetic operation.
    """
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


if __name__ == "__main__":
    print(pFEval("6 3 2 4 + - *"))
