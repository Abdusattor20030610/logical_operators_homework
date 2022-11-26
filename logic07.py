def main(a,b):
    x=a>0 or b<0
    y=a<0 or b>0
    z=a<0 or b<0
    return x or y or z
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
print(main(-3,8))