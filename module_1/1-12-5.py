a = int(input())
b = int(input())
c = int(input())
if (a >= b >= c):
    max = a
    sr = b
    min = c
elif (a >= c >= b):
    max = a
    sr = c
    min = b
elif (b >= a >= c):
    max = b
    sr = a
    min = c
elif (b >= c >= a):
    max = b
    sr = c
    min = a
elif (c >= a >= b):
    max = c
    sr = a
    min = b
elif (c >= b >= a):
    max = c
    sr = b
    min = a
print(max)
print(min)
print(sr)