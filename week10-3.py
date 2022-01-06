def reverse(x):
    if len(x)==1:
        return x[0]
    else:
        return(x[-1]+reverse(x[:-1]))
print(reverse('apple'))
