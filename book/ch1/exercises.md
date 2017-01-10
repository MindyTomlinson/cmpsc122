# Chapter 1 Exercises

## Reinforcement Exercises

### R-1.8
If string s has length n, and expression s[k] is used for index -n <= k < 0, what is the
equivalent index j >= 0 such that s[j] references the same element?

j = n + k

s = 'abcdefg'
k = -2
n = 7
j = 7 + -2 = 5
s[k] = s[-2] = 'f'
s[j] = s[5] = 'f'


### R-1.9
What parameters should be sent to the range constructor to produce a range with values
50, 60, 70, 80?

```python
[k for k in range(50,90,10)]
```

### R-1.10
What parameters should be sent to the range constructor to produce a range with values
8, 6, 4, 2, 0, -2, -4, -6, -8?

```python
[k for k in range(8,-10,-2)]
```

### R-1.11
How to use list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]?

```python
[2**k for k in range(9)]
```


## Creativity Exercises

### C-1.13
Pseudo-code function that reverses a list of n integers

```python
def reverses(seq):
  n = len(seq)
  return [seq[n-j-1] for j in range(n)]
```

### C-1.14

```python
def is_odd(k):
    """Takes an integer and determines if it is odd"""
    return k % 2 == 1

def any_odd_products(seq):
    """Takes a sequence of integers and determines if there's a distinct pair
    of values whose product is odd (take 2)"""
    odds = sum([is_odd(k) for k in seq]) # Count how many odd numbers in seq
    return odds >= 2 # If there's 2 or more odd numbers, then they'll produce an odd product
```

### C-1.15

```python
def are_all_unique(seq):
    """Takes a sequence and determines if they're all unique values"""
    return len(seq) == len(set(seq))
```

### C-1.16

In our implementation of the scale function (page 25), the body of the loop executes the command `data[j] *= factor`. We have discussed that numeric types are immutable, and that use of the = operator in this context causes the creation of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation of scale changes the actual parameter sent by the caller?

 Answer:
 When the command `data[j] *= factor` is called, the value in data[j] is immutable, and when multiplied by factor, the result is a new instance of a number. But the jth "slot" in data is not immutable -- it can point to the new number instance.

### C-1.18

Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

 0 - 2*0
 2 - 2*0 + 2*1
 6 - 2*0 + 2*1 + 2*2
12 - 2*0 + 2*1 + 2*2 + 2*3
20 - 2*0 + 2*1 + 2*2 + 2*3 + 2*4
30 - 2*0 + 2*1 + 2*2 + 2*3 + 2*4 + 2*5
42 - 30 + 2*6
56 - 42 + 2*7
72 - 56 + 2*8
90 - 72 + 2*9

 0 = 2 * (0)
 2 = 2 * (0 + 1)
 6 = 2 * (0 + 1 + 2)
12 = 2 * (0 + 1 + 2 + 3)
20 = 2 * (0 + 1 + 2 + 3 + 4)
...
90 = 2 * (0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)

Answer:
```python
[2 * sum(range(i)) for i in range(n)]
```

### C-1.19

Demonstrate how to use Python’s list comprehension syntax to produce the list ['a', 'b', 'c', ..., 'z'], but without having to type all 26 such characters literally.

Hint: Use the chr() function

```python
print([ord(c) for c in 'abcdefghijklmnopqrstuvwxyz']) # Find numeric equivalent
# ord() is the inverse of chr()

[chr(i) for i in range(97,123)]
```

### C-1.20

Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.

```python
import random

def swap(seq):
  n = len(seq)
  for i in range(n):
    swap_with = random.randint(0, n-1)
    seq[i], seq[swap_with] = seq[swap_with], seq[i]
```

### C-1.21

Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D).

1.  Read lines (while True)?
2.  Stores lines in list
3.  Catch EOFError, handle it
4.  Output lines from list in reverse order

```python
lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    lines.reverse()
    print(*lines, sep="\n") # The *lines is a "starred expression"

# https://stackoverflow.com/questions/12555627/python-3-starred-expression-to-unpack-a-list
```
