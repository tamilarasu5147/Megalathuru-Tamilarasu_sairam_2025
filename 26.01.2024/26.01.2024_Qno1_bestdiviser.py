'''
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.
'''
#logic1
#!/bin/python3

import math
import os
import random
import re
import sys


def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def best_divisor(n):
    best_divisor = 1
    max_digit_sum = 1

    for i in range(2, n + 1):
        if n % i == 0:
            current_digit_sum = digit_sum(i)
            if current_digit_sum > max_digit_sum or (current_digit_sum == max_digit_sum and i < best_divisor):
                max_digit_sum = current_digit_sum
                best_divisor = i

    return best_divisor

if __name__ == '__main__':
    n = int(input().strip())
    result = best_divisor(n)
    print(result)


#logic2
def digit_sum(num):
    return sum(map(int, str(num)))

def best_divisor(n):
    best_div = 1
    max_digit_sum = 1

    for i in range(2, n + 1):
        if n % i == 0:
            current_digit_sum = digit_sum(i)
            if current_digit_sum > max_digit_sum or (current_digit_sum == max_digit_sum and i < best_div):
                max_digit_sum = current_digit_sum
                best_div = i

    return best_div

if __name__ == '__main__':
    n = int(input().strip())
    result = best_divisor(n)
    print(result)
