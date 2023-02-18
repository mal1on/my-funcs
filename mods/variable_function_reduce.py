from operator import add, sub
from re import findall


def my_reduce(operators, numbers):
    nums = iter(numbers)
    ops = iter(operators)
    value = next(nums)
    for element in nums:
        op = next(ops)
        match op:
            case '+':
                function = add
            case '-':
                function = sub
            case '=':
                def function(a, b): return b
        value = function(value, element)
    return value
