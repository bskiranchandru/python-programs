for i in range(1,70):
    print("=",end='')
    
print("\n")
print("USING TEMP variable")
a=2
b=1
print("Before swaping a=",a,"b=",b)
t=a
a=b
b=t
print("After swaping a=",a,"b=",b)
for i in range(1,70):
    print("=",end='')
print("\n")
print("without using temp variables")
a=1
b=2
print("Before swaping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("After swaping a=",a,"b=",b)
for i in range(1,70):
    print("=",end='')

