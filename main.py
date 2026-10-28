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

def decimal_to_binary_steps(n):
    """Calculating and printing the binary conversion steps (used for explanations)."""
    if n == 0:
        print("0 in binary is 0")
        return "0"
    
    current_n = n
    binary_result = ""
    
    while current_n > 0:
        quotient = current_n // 2
        remainder = current_n % 2
        print(f"{current_n} // 2 = {quotient}, remainder = {remainder}")
        binary_result = str(remainder) + binary_result
        current_n = quotient
    print(f"Correct binary representation: {binary_result}\n")

def practice_mode():
    """Running an interactive loop for practicing questions."""
    score = 0
    total = 0
    
    print("=== Welcome to NumberSense Practice Mode! ===")
    print("Type 'q' anytime to quit.\n")
    
    while True:
        num1 = random.randint(10, 999)
        num2 = random.randint(10, 999)
        
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

def practice_binary_mode():
    """Running an interactive quiz loop for decimal to binary conversion."""
    score = 0
    total = 0
    
    print("=== Welcome to Binary Conversion Practice! ===")
    print("Type 'q' anytime to quit.\n")
    
    while True:
        target_num = random.randint(5, 9999)
        
        # Calculating correct binary answer beforehand
        temp_n = target_num
        correct_binary = ""
        while temp_n > 0:
            rem = temp_n % 2
            correct_binary = str(rem) + correct_binary
            temp_n = temp_n // 2
            
        user_input = input(f"Convert decimal number {target_num} to binary: ")
        
        if user_input.lower() == 'q':
            print(f"\nBinary Practice Over! Your score: {score} out of {total}")
            break
            
        try:
            user_answer = int(user_input)
            total += 1
            
            if user_answer == int(correct_binary):
                print("Correct! Great job. 🎉\n")
                score += 1
            else:
                print(f"Not quite. The correct binary for {target_num} is {correct_binary}.")
                print("Here is how the division steps work out:")
                decimal_to_binary_steps(target_num)
                
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.\n")

if __name__ == "__main__":
    practice_mode()
if __name__ == "__main__":
    practice_binary_mode()