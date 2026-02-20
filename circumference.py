def pi_math():
    pi = 3.14
    
def calculate_circumference(radius):
    circumference = 2 * pi_math * radius
    return circumference

r = float(input("Enter the radius of the circle: "))
result = calculate_circumference(r)
print("The circumference of the circle is:", result)