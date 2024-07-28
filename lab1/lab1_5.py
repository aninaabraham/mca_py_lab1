def e_s(s, e):
    for i in range(s, e):
        if i % 2 == 0:
            print(f"Number: {i}, Square: {i**2}")


print("Range (1, 50):")
e_s(1, 50)

print("\nRange (1, 100):")

e_s(1, 100)

