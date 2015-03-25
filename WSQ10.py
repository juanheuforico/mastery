#Juan Antonio Olvera Robles
import math
import statistics

awn=1
lis=[]
while(awn!='n'):
    ad=float(input("give me a number to put it in a list"))
    lis.append(ad)
    awn=str(input("do you want add another number? put n for no"))
def dev(ad):
    suma=0
    print(lis)
    print(len(lis))
    for i in range(0,len(lis)):
        suma=suma + lis[i]
    average=suma/len(lis)
    dev=average**.5
    return dev

print("standard deviation", dev(ad))
