#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    result = a
    for i in range(1, abs(b)):
        result = result * a
    if b < 0:
        return (1 / result)
    return result
