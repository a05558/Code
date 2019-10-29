#!/usr/bin/env python3

n = 10
sum = 0
count = 0
print("please input 10 numbers:")
while count < n:
    number = float(input())
    sum += number
    count += 1
average = sum / n
print("N = %d, Sum = %.1f" % (n, sum))
print("Average = {:.2f}".format(average))


