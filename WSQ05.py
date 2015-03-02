tem=int(input("give me the temperature in Fahrenhei."))
c=5*(tem-32)/9
print("la temperatura en celsius es ",c)
if c < 100:
    print("Water does not boil at this temperature (under typical conditions).")
else:
    print("Water does boil at this temperature (under typical conditions).")
