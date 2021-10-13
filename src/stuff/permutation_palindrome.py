from collections import Counter
import string

def is_palindrom_perm(word):
    """
        Check if a permutation of a string is a palindrome
        Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards
    """
    clean_w = sanitize(word)
    print(clean_w)
    ctr = Counter(clean_w)
    print(ctr)
    odd_c = sum(x%2 for x in ctr.values())
    print(odd_c)
    return odd_c in [0,1]

    
def sanitize(x: str) -> str:
    only_letter_filter = filter(lambda c: c.isalpha(), x.strip())
    res = "".join(map(lambda c: c.lower(), only_letter_filter))
    return res


res = is_palindrom_perm('aaabccbbadx')
print(res)
    