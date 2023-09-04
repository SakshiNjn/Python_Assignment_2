def area(len_side):
    area = len_side ** 2
    return area

len_side = float(input("Enter length of side of a the square: "))

area_of_square = area(len_side)

print(f"The area of the square with side length {len_side} is: {area_of_square}")
