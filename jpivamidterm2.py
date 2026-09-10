#Janelle Piva
#Midterm 2

def rectangleArea(rectangle_base, rectangle_height):
    area = rectangle_base * rectangle_height
    return area

base = int(input("Enter the base of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

answer = rectangleArea(base, height)

print("The area of the rectangle is", answer)
