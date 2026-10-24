print("Welcome to NumberSense!")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"You entered: {a} and {b}")

def gcd_steps(a, b):
    while b != 0:
        quotient = a // b
        remainder = a % b
    
        print(f"{a} = {b} * {quotient} + {remainder}")
    
        a = b
        b = remainder

    print(f"GCD = {a}")
gcd_steps(a, b)