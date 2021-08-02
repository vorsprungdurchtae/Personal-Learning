#!/bin/python

import math
import os
import random
import re
import sys

"""
Task 
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  2 to 5, print Not Weird
If  is even and in the inclusive range of  6 to 20, print Weird
If  is even and greater than 20, print Not Weird


"""

def exp(x):
    if (x % 2 != 0):
        print("Weird")
    else:

        if (6 <= x <= 20):
            print("Weird")
        else:
            print("Not Weird")


if __name__ == '__main__':
    n = int(raw_input().strip())
    exp(n)
