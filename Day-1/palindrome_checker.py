def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

while True:
    user_input = input("\nEnter a string or number to check (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break    
    if is_palindrome(user_input):
        print(f"'{user_input}' is a Palindrome!")
    else:
        print(f"'{user_input}' is NOT a Palindrome.")
