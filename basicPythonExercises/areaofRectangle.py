import math
#Calvculate rectangle area
def calculateArea(length,width):
    area=length*width
    return area
print("\n Welcome to Rectangle Area Calculator!\n")
rectangleLength=float(input("Enter Rectangle Length : "))
rectangleWidth=float(input("Enter Rectangle Width : "))
area=calculateArea(rectangleLength,rectangleWidth)
print(f"The area is {math.floor(area)} cm^2")