def main(a):
    return (a//100+a//10%10+a%10)%2!=0
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
print(main(152))