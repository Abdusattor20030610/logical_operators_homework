def main(a,b):
    a=a%2==1
    b=b%2==1
    return a and b
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
print(main(3,8))