def fizz_buzz(num):
    """
    Returns 'Fizz' if the num parameter is divisible by 3,
    'Buzz' if the num is divisible by '5',
    'FizzBuzz' if the num is divisible by 3 and 5,
    and returns num for any other number.

    Args:
    num (int): The number to check.

    Returns:
    str or int: The corresponding string or the number itself.
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

while True:
    user_input = input("Enter a number or 'q' to quit: ")

    if user_input.lower() == 'q':
        break

    try:
        num = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a number or 'q' to quit.")
        continue

    result = fizz_buzz(num)
    print(result)
