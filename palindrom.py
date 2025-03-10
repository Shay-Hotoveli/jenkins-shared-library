def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Example number to test
number = 12321  

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
