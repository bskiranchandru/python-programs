def smallest(x):
    if len(x)==1:
        return x[0]
    elif x[0]<smallest(x[1:]):
        return x[0]
    else:
        return smallest(x[1:])

print(smallest([10,20,40,66,6,5,8]))
