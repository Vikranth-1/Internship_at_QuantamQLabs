def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    try:
        sum_of_powers = sum(int(digit) ** n for digit in num_str)
        return sum_of_powers == num
    except ValueError:
        return False

while True:
    user_input = input("\nEnter an integer to check (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break    
    try:
        num = int(user_input)
        if num < 0:
            print("Armstrong numbers are typically defined for non-negative integers.")
            continue    
        if is_armstrong(num):
            num_str = str(num)
            n = len(num_str)
            calc_str = " + ".join(f"{digit}^{n}" for digit in num_str)
            print(f"{num} is an Armstrong number! ({calc_str} = {num})")
        else:
            num_str = str(num)
            n = len(num_str)
            calc_str = " + ".join(f"{digit}^{n}" for digit in num_str)
            sum_val = sum(int(digit) ** n for digit in num_str)
            print(f"{num} is NOT an Armstrong number. ({calc_str} = {sum_val} != {num})")
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'exit'.")
