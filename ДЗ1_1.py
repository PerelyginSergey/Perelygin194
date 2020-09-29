import math
a = float(input("параметр a равен:"))

def I_1(n):
    if n == 0:
        return math.log( (a+1)/a )

    return 1/n -a * I_1(n-1)

print("по прямой реккурсии",I_1(25))

def I_2(n):

    if n == 50:
        return 0
    return (1/(n+1) - I_2(n+1))/a

print("по обратной реккурсии", I_2(25) )

