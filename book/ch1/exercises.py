import random
import itertools

def is_multiple(n, m):
    """Takes 2 integer values and returns True if n is multiple of m"""
    return m % n == 0

def is_even(k):
    """Takes an integer k and returns True if k is even, but without
    using multiplication, division, or modulo operators"""
    if k == 0:
        return True
    elif abs(k) == 1:
        return False
    else:
        return is_even(abs(k) - 2)

def minmax(data):
    """Takes a sequence of 1 or more numbers and returns a tuple of the
    min and max, but without using built-in min() and max() functions"""
    low = high = data[0]
    for value in data:
        if value > high:
            high = value
        if value < low:
            low = value
    return (low, high)

def sumsquares(n):
    """Takes a positive integer n and returns the sum of squares for all
    positive integers smaller than n"""
    return sum([x * x for x in range(n)])

def oddsumsquares(n):
    """Takes a positive integer n and returns the sum of squares for all
    odd positive integers smaller than n"""
    return sum([x * x for x in range(n) if x % 2 == 1])

def choice(seq):
    """Implements the random.choice function using only random.randrange"""
    n = len(seq)
    i = random.randrange(n)
    return seq[i]

def isoddproduct(a,b):
    """Takes two numbers and determines if their product is odd"""
    return a * b % 2 == 1

def oddpairs(seq):
  """Takes a sequence of integers and determines if there's a distinct pair
  of values whose product is odd"""
  pairs = itertools.combinations(seq, 2)
  return any(isoddproduct(a,b) for a,b in pairs)

def is_odd(k):
    """Takes an integer and determines if it is odd"""
    return k % 2 == 1

def any_odd_products(seq):
    """Takes a sequence of integers and determines if there's a distinct pair
    of values whose product is odd (take 2)"""
    odds = sum([is_odd(k) for k in seq]) # Count how many odd numbers in seq
    return odds >= 2 # If there's 2 or more odd numbers, then they'll produce an odd product

def are_all_unique(seq):
    """Takes a sequence and determines if they're all unique values"""
    return len(seq) == len(set(seq))

def swap(seq):
    n = len(seq)
    for i in range(n):
        swap_with = random.randint(0, n-1)
        seq[i], seq[swap_with] = seq[swap_with], seq[i]

def dot_product(a,b):
    return [ai * bi for ai, bi in zip(a,b)]

def contains_a_vowel(sentence):
    return any(vowel in sentence for vowel in 'AEIOUaeiou')

def remove_punctuation(sentence):
    punctuation = "`~!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"
    return "".join(chr for chr in sentence if chr not in punctuation)

if __name__ == '__main__':
    print("R-1.1: is_multiple(3, 12) =", is_multiple(3, 12))
    print("R-1.2: is_even(9) =", is_even(9))
    print("R-1.2: is_even(8) =", is_even(8))
    print("R-1.3: minmax([5, 2, 1]) =", minmax([5, 2, 1]))
    print("R-1.3: minmax([19]) =", minmax([19]))
    print("R-1.4: sumsquares(4) =", sumsquares(4), "(should equal 14)")
    print("R-1.6: oddsumsquares(6) =", oddsumsquares(6), "(should equal 35)")
    print("R-1.12: set of random choices from (0,1,2) =")
    print([choice((0,1,2)) for i in range(20)])
    print("C-1.14: any_odd_products([2,4,6]) =",
    any_odd_products([2,4,6]), "(should be False)")
    print("C-1.14: any_odd_products([1,2,5]) =",
    any_odd_products([1,2,5]), "(should be True)")
    print("C-1.15: are_all_unique([1,2,3]) =", are_all_unique([1,2,3]))
    print("C-1.15: are_all_unique([1,1,9]) =", are_all_unique([1,1,9]))
    print("C-1.24: contains_a_vowel('yes') =",
    contains_a_vowel('yes'), "(should be True)")
    print("C-1.24: contains_a_vowel('mmhmm') =",
    contains_a_vowel('mmhmm'), "(should be False)")
    print("C-1.25: remove_punctuation(\"What's the *point*?\") =",
    remove_punctuation("What's the *point*?"))
