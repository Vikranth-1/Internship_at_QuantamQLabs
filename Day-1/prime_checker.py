import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

while True:
    user_input = input("\nEnter a positive integer to check (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break    
    try:
        num = int(user_input)
        if num < 0:
            print("Please enter a positive integer.")
            continue
        if is_prime(num):
            print(f"{num} is a Prime Number.")
        else:
            print(f"{num} is NOT a Prime Number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'exit'.")
