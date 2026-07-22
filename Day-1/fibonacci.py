def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

while True:
    user_input = input("\nEnter the number of Fibonacci terms to generate (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break   
    try:
        n = int(user_input)
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            continue           
        fib_series = generate_fibonacci(n)
        print(f"Fibonacci series of {n} terms:")
        print(", ".join(map(str, fib_series)))
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'exit'.")
