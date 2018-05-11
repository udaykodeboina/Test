class cal():#'creating a cal class'
    def __init__(self,a,b):#'creating a userdefined function'
        self.a=a
        self.b=b
    def add(self):#'creating a userdefined add function'
        return self.a+self.b
    def mul(self):#'creating a userdefined multiplication function'
        return self.a*self.b
    def div(self):#'creating a userdefined division function'
        return self.a/self.b
    def sub(self):#'creating a userdefined sub function'
        return self.a-self.b
a=int(input("Enter first number: "))#'enter first input that should be int type'
b=int(input("Enter second number: "))#'enter second input that should be int type'
obj=cal(a,b)#'creating a object to the class'
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))#'enter choice that should be int type'
    if choice==1:#'if choice equal to 1 perform add function and print result'
        print("Result: ",obj.add())
    elif choice==2:#'if choice equal to 2 perform sub function and print result'
        print("Result: ",obj.sub())
    elif choice==3:#'if choice equal to 3 perform mul function and print result'
        print("Result: ",obj.mul())
    elif choice==4:#'if choice equal to 4 perform div function and print result'
        print("Result: ",round(obj.div(),2))
    elif choice==0:#'if choice equal to o print exiting'
        print("Exiting!")
    else:#'print invalid choice'
        print("Invalid choice!!")
 
 
print()
