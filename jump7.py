a = 0
while a < 100:
    a += 1
    if a % 7 and not '7' in str(a):
        print(a)
