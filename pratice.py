user_input = input("Please enter a number: ")
try:
    user_input_int = int(user_input)
    print("You entered the integer:", user_input_int)
except ValueError:
    print("The input is not a valid integer.")