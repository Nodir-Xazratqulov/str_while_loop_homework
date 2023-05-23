def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    i=0
    while i<len(s):
        if int(s[i])%2==1:
            k+=int(s[i])
        i+=1
    return k
print(main('1234567'))