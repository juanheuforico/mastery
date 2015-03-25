#Juan Antonio Olvera Robles
def triangles(size):
    for r in range(1,size +1):
        for c in range(1,r+1):
            print("t",end="")
        print()
    for r in range(size-1,0,-1):
        for c in range(1,r+1):
            print("t",end="")
        print()
    return(c)
size=int(input("dame un numero:"))
t=triangles(size)
