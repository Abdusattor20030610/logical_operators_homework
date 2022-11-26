def main(a,b):
    x=a>0 and b>0
    y=a<0 and b<0
    return x or y

    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
print(main(4,-4))