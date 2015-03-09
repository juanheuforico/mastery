def fact(n):
        fac=1
        if n < 0:
            print("factorial does not exist for negative numbers")
        elif n == 0:
            print("the factorial of 0 is 1")
        else:
            for i in range(1,n + 1):
                fac=fac*i
        return fac
an='y'
while (an=='y'):
    n=int(input("giveme a number to get its factorial"))
    if (n > 0):
        print("the factorial of ",n," is",fact(n))
    else:
        fact(n)
    an=str(input("do you want try it again? (y/n)"))
print("have a nice day")
