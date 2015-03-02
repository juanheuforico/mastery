import random
p=random.randrange(100)
print(p)
con=1
print("I have a number chosen between 1 and 100.")
r=int(input("Please guess a number between 1 and 100: "))
#print=random.randrange(100)
while r != p:
    if r < p:
        r=int(input("the number that you are searching is morehigh "))
    if r > p:
        r=int(input("the number that you are searching is lower "))
    con=con+1
print("You got it! The right answer is indeed ",r)
print("you do ",con,"trys")
