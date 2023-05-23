def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """

    a='aeiou'
    i=0
    k=0
    while i<len(s):
        if s[i].isalpha() and s[i] not in a:
            k+=1
        i+=1
    return k
print(main('Codeschoolsuz'))

