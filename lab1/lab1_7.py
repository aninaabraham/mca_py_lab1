import math

# Function to calculate the area of a triangle 
def area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# first triangle
a1 = int(input("Enter the first side of the first triangle: "))
b1 = int(input("Enter the second side of the first triangle: "))
c1 = int(input("Enter the third side of the first triangle: "))

#  second triangle
a2 = int(input("Enter the first side of the second triangle: "))
b2 = int(input("Enter the second side of the second triangle: "))
c2 = int(input("Enter the third side of the second triangle: "))


area1 = area(a1, b1, c1)
area2 = area(a2, b2, c2)

# Calculate total area and contributions
total_area = area1 + area2
contribution1 = (area1 / total_area) * 100
contribution2 = (area2 / total_area) * 100


print("Area of the first triangle: {:.2f}".format(area1))
print("Area of the second triangle: {:.2f}".format(area2))
print("Total area enclosed by both triangles: {:.2f}".format(total_area))
print("First triangle's contribution: {:.2f}%".format(contribution1))
print("Second triangle's contribution: {:.2f}%".format(contribution2))
