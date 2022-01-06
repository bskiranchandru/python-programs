dd=int(input())
yy=int(input())
mm=int(input())
if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(mm==2 and yy%400==0):
    max1=29
elif mm==2:
    max1=28
elif dd<1  or dd>31:
    print('invalid date')
elif mm<1 or mm>12:
    print('invalid date')
elif (mm==12 and dd==31):
    yy=yy+1
    mm=1
    dd=1
    print(dd,mm,yy,)
elif (dd==31 and mm!=12):
    dd=1
    mm=mm+1
    print(dd,mm,yy)
else:
    dd=dd+1
    print(dd,mm,yy)
    
    
