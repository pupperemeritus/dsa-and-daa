def toh(n: int, src: str, aux: str, dest: str) -> int:
    """
    Recursive function to solve the Tower of Hanoi problem.

    Parameters:
        n (int): The number of discs.
        src (str): The source peg.
        aux (str): The auxiliary peg.
        dest (str): The destination peg.

    Returns:
        int: The minimum number of moves required to solve the problem.
    """
    # Base case: If there are no discs, return.
    if n == 0:
        return 0
    
    # Move n-1 discs from source to auxiliary peg.
    toh(n-1, src, dest, aux)
    
    # Move the nth disc from source to destination peg.
    print(f"Move disc {n} from {src} to {dest}")
    
    # Move the n-1 discs from auxiliary to destination peg.
    toh(n-1, aux, src, dest)
    
    # Return the total number of moves required.
    return (2**n) - 1


if __name__ == "__main__":
    n = int(input("Enter n : "))
    n_steps = toh(n, "A", "B", "C")
    print(n_steps)
