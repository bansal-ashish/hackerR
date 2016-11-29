#!/usr/bin/env python
"""
Given an array of N integers, can you find the sum of its elements?

Input Format
The first line contains an integer, N, denoting the size of the array.
The second line contains N space-separated integers representing the array's
elements.

Output Format
Print the sum of the array's elements as a single integer.

Sample Input
6
1 2 3 4 10 11

Sample Output
31

Explanation
We print the sum of the array's elements, which is: 1+2+3+4+10+11=31.
"""
from __future__ import print_function


try:
    input = raw_input
except:
    pass


def main():
    array_size = int(input().strip())
    array = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    print(sum(array))


if __name__ == '__main__':
    main()