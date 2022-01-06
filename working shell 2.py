'''s=input()
s2=input()
a=list(set(s)&set(s2))
print(a)
for i in a:
    print(i)'''
'''s=set([chr(a) for a in range(ord('a'),ord('z')+1)])
print(s)'''
'''a={'a':1,'b':2,'c':3}
print([a['a']])
for i in a:
    print(i,'=',a[i])
a=10
b=bin(a)
print(b)
print('next')'''
a=int(input())
for i in range(0,a):
     y=i/2
     x=y%2
print(x,end=' ')
     
