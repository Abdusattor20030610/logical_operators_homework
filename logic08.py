def main(a,b):
    x=a%2==0 
    y=b%2==0
    return x or y
"""
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
print(main(6,8))