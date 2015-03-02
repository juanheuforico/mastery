
print("give me  a range of integers to prints the sum of the numbers in that range ")
r1=int(input("value to star "))
r2=int(input("value to finish "))
cont= r1
acum=r1
while cont<r2:
    cont=cont+1
    acum=acum+1
    r1=r1+acum
    print(r1)
