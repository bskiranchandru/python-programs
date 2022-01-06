p=int(input())
r=int(input())
t=int(input())
si=(p*t*r)/100
amt=p*(1+(r/100))**t
comp=amt-p
print(si,comp)
