lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    lines.reverse()
    print(*lines, sep="\n") # The *lines is a "starred expression"

# https://stackoverflow.com/questions/12555627/python-3-starred-expression-to-unpack-a-list
