def main(a):
    return a//10000>a//1000%10>a//100%10>a//10%10
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
print(main(75421))