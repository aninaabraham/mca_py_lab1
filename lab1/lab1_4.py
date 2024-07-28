colour = ["Black", "Red", "Maroon", "Yellow"]
code = ["000000", "FF0000", "800000", "FFFF00"]


result = [{"colorName": name, "colorCode": code} for name, code in zip(colour, code)]



print("\nList of Dictionaries:")
for item in result:
    print(item)
