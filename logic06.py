def main(a,b):
    x=a>0 or b<0
    y=a<0 or b>0
    return x or y
print(main(-3,8))

"""
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """