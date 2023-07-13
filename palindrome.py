from stack import Stack


def palindrome(word: str) -> bool:
    """
    Check if a word is a palindrome.

    Args:
        word (str): The word to check for palindrome.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    stack = Stack(100)  # Create a stack to store the characters of the word
    for i in word:  # Push each character of the word onto the stack
        stack.push(i)
    wordrev = ""  # Variable to store the reversed word
    while (
        not stack.isEmpty()
    ):  # Pop each character from the stack and append to wordrev
        wordrev += stack.pop()
    return (
        word == wordrev
    )  # Return True if the word is equal to its reverse, False otherwise


if __name__ == "__main__":
    if palindrome(input("Enter Word : ")):
        print("It is a Palindrome")
    else:
        print("It is not  a Palindrome")
