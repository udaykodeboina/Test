date=input("Enter the date: ")#'enter the date that should be int type'
dd,mm,yy=date.split('/')#'dd mm yy separated by "/" i.e dd/mm/yy'
dd=int(dd)#'date should be int type'
mm=int(mm)#'month should be int type'
yy=int(yy)#'year should be int type'
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):#"if mm=1,2,5,7,8,10,12 max days=31"
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):#"if mm=4,6,9,11 max days=30"
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400==0):#'year/4&y/100!=0&y/400=0 max days is29"
    max1=29
else:#"elsedays=28"
    max1=28
if(mm<1 or mm>12):#"if mm less than 1 and greater than 12 print date is invalid"
    print("Date is invalid.")
elif(dd<1 or dd>max1):#"if dd less than 1 and greater than max1(31) print date is invalid"
    print("Date is invalid.")
elif(dd==max1 and mm!=12):#"if dd =max 1 and month!=12 print date=1&mm+1&yy"
    dd=1
    mm=mm+1
    print("The incremented date is: ",dd,mm,yy)
elif(dd==31 and mm==12):#"if dd =max 1 and month=12 print date=1&mm=1&yy=yy+1"
    dd=1
    mm=1
    yy=yy+1
    print("The incremented date is: ",dd,mm,yy)
else:#'else dd=dd+1'
    dd=dd+1
    print("The incremented date is: ",dd,mm,yy)
