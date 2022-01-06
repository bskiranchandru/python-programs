a=float(input('enter co eff of x^2'))
b=float(input('enter co eff of x'))
c=float(input('enter co eff of x^0'))
if (a==0):
    print('the equation is not quadratic')
d=b**2-(4*a*c)
if (d>0):
    print('the roots are distinct')
elif (d==0):
    print('roots are equal')
else:
    print('the roots are imaginary')
r1=((-1)*b+d**0.5)/(2*a)
r2=((-1)*b-d**0.5)/(2*a)
print('the equation is',a,'x^a+',b,'x+',c)
print('root 1= ',r1)
print('root 2= ',r2)
