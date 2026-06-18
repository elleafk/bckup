weight = input("Weight: ")
unit = input("K(g) or L(bs): ").upper()

if unit == "K":
    converted = float(weight) / 0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = float(weight) * 0.45
    print("Weight in kg: " + str(converted))
