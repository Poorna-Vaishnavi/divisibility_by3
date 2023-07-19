def is_divisible_by_3(a):
    b=0
    for digit in a:
        b+=digit
    if b%3==0:
        return 1
    else:
        return 0
a=list(map(int,input().split()))
print(is_divisible_by_3(a))

