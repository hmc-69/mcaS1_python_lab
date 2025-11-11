calculate_sq_area = lambda side_length: side_length**2
calculate_rect_area = lambda length,width: length*width
calculate_tri_area = lambda base,height:0.5*base*height

sqs=int(input("Enter the side of sqaure: "))

print("Enter the base and height of triangle: ")
ht=int(input("Height: "))
bs=int(input("Base: "))

print("Enter the length and breadth of rectangle: ")
l=int(input("Length: "))
b=int(input("Breadth: "))

sq_area=calculate_sq_area(sqs)
print("Area of Square: ",sq_area)

tri_area=calculate_tri_area(bs,ht)
print("Area of Triangle : ",tri_area)

rect_area=calculate_rect_area(l,b)
print("Area of square: ",rect_area)
