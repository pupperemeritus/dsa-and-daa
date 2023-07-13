def kmp(text, pattern):
    """
    Knuth-Morris-Pratt algorithm for pattern matching.

    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.

    Returns:
        list: A list containing a boolean indicating whether the pattern was found in the text,
              and a list of indices where the pattern was found.
    """
    tLen = len(text)
    pLen = len(pattern)
    found = False
    lps = [0] * pLen
    foundat = []
    computeLPS(pattern, pLen, lps)
    i = j = 0

    while i < tLen:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == pLen:
            found = True
            foundat.append(i - j)
            j = lps[j - 1]
        elif i < tLen and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return [found, foundat]


def computeLPS(pattern, m, LPS):
    """
    Compute the Longest Proper Prefix which is also a Suffix (LPS) array for a given pattern.

    Args:
        pattern (str): The pattern string.
        m (int): The length of the pattern.
        LPS (list): An array to store the computed LPS values.

    Returns:
        None. The LPS array is modified in place.

    """
    length = 0  # Initialize the length of the longest common prefix suffix
    i = 1  # Start from the second character of the pattern
    LPS[0] = 0  # The LPS value for the first character is always 0

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1  # Increment the length of the common prefix suffix
            LPS[i] = length  # Store the length in the LPS array
            i += 1  # Move to the next character
        else:
            if length != 0:
                length = LPS[
                    length - 1
                ]  # Update the length based on previously computed values
            else:
                LPS[i] = 0  # If there is no common prefix suffix, set the length to 0
                i += 1  # Move to the next character


if __name__ == "__main__":
    print(kmp(input(), input()))
