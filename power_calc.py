def power_calculator():
    print("=== Power Calculator ===")
    
    base = int(input("Enter the number: "))
    exponent = int(input("Enter the power: "))
    
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    
    if exponent < 0:
        result = 1 / result
    
    print("Result:", result)

power_calculator()