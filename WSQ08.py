n1=int(input("give me a number"))
n2=int(input("give me other number"))
def misuma(n1,n2):
    suma=n1+n2
    return suma

def mires(n1,n2):
    res=n1-n2
    return res
def miprod(n1,n2):
    prod=n1*n2
    return prod
def midiv(n1,n2):
    div=int(n1/n2)
    return div
def mirem(n1,n2):
    rem=int(n1%n2)
    return rem
print("the sum of your numbers is ", misuma(n1,n2))
print("the difference of your numbers is ", mires(n1,n2))
print("the product of your numbers is ", miprod(n1,n2))
print("the division of your numbers is ", midiv(n1,n2))
print("the remainder of your numbers is ", mirem(n1,n2))
