def desc_order(num):
    li=[]
    for i in str(num):
        li.append(i)
    li.sort()
    a=li[::-1]
    b=int(''.join(map(str,a)))
    print(b)
    print(type(b))
a=int(input("Enter the number to be ordered:"))
desc_order(a)
