import random

def calculate_gcd(a, b):
    """Calculating and returning the GCD without printing steps."""
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def gcd_steps(a, b):
    """Calculating GCD and printing each step (used only when explaining incorrect answers)."""
    if a < b:
        a, b = b, a
        
    while b != 0:
        quotient = a // b
        remainder = a % b
        print(f"{a} = {b} × {quotient} + {remainder}")
        a = b
        b = remainder
    return a

def practice_mode():
    """Running an interactive loop for practicing questions."""
    score = 0
    total = 0
    
    print("=== Welcome to NumberSense Practice Mode! ===")
    print("Type 'q' anytime to quit.\n")
    
    while True:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        
        # 1. Get the correct answer without printing steps
        actual_gcd = calculate_gcd(num1, num2)
        
        # 2. Asking input from the user before showing him any working
        user_input = input(f"What is the GCD of {num1} and {num2}? (or type 'q' to quit): ")
        
        if user_input.lower() == 'q':
            print(f"\nGame Over! Your final score: {score} out of {total}")
            break
            
        try:
            user_answer = int(user_input)
            total += 1
            
            if user_answer == actual_gcd:
                print("Correct! Great job. 🎉\n")
                score += 1
            else:
                print(f"Not quite. The correct GCD was {actual_gcd}.")
                print("Here is how the steps work out:")
                # 3. ONLY printing the steps here, because user got it wrong!
                gcd_steps(num1, num2)
                print()
                
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.\n")

if __name__ == "__main__":
    practice_mode()