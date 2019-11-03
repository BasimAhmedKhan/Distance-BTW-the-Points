print(" ")
print('"Python Program To Compute The Distance Between The Points (x1, y1) and (x2, y2)"')
print(" ")

val1 = float(input("Enter Point(x1): "))
print(" ")

val2 = float(input("Enter Point(y1): "))
print(" ")

val3 = float(input("Enter Point(x2): "))
print(" ")

val4 = float(input("Enter Point(y2): "))
print(" ")

print('"By Using Distance Formula!"')
print(" ")

ans = (((val3 - val1)**2 + (val4 - val2)**2)**0.5)

print("Distance = " + str(ans) + " units")
print(" ")