x=str(input())
if x=='�������������':
    a=int(input())
    b=int(input())
    print(a*b)
elif x=='�����������':
    a=int(input())
    b=int(input())
    c=int(input())
    p=(a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif x=='����':
    r=int(input())
    print(3.14*(r**2))