import functools
s=input('enter a few words').split()
p=sorted(s,key=len)
print(p[-1])
b=input('enter a suffix')
print(list(filter((lambda x:x.endswith(b)),s)))
c=input('enter a prefix')
print(list(filter((lambda x:x.startswith(c)),s)))
sub_string=input('enter a word: ')

print(list(filter(lambda x:sub_string in x,s)))
l=len(s)
f=list(map(len,s))
r=functools.reduce(lambda x,y:x+y,f)
print(r/l)
