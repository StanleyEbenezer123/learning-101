# coding=utf-8
"""
Problem Statement: Fizz Buzz - Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
"""
i = 1
while i <= 100:
    if (i % 3 == 0) and (i % 5 == 0):
        print "fizzbuzz"
    elif i % 3 == 0:
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i
    i += 1
