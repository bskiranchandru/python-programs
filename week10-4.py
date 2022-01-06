def fl(x):
    r=1
    for i in range(1,x+1):
        r=i*r
    return r

def fr(x):
    r=[]
    for i in range(1,x+1):
        if x%i==0:
            r.append(i)
    return r

def eo(x):
    if(x%2==0):
        return 'even'
    else:
        return 'odd'

def p(x):
    s=fr(x)
    if len(s)>2:
        return 'not prime'
    else:
        return 'prime'

n=int(input('enter a no.:'))
print(fl(n))
print(fr(n))
print(eo(n))
print(p(n))
