def desc_order(num):
    li=[]
    for i in str(num):
        li.append(i)
    li.sort()
    a=li[::-1]
    b=int(''.join(map(str,a))) #returns an integer using list members
    print(b)
    print(type(b))
a=int(input("Enter the number to be ordered:"))
desc_order(a)            
#Sample i/p:123456789
#Sample o/p:987654321
