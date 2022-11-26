def main(a):
    return (a//10+a%10)%2==1
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
print(main(45))