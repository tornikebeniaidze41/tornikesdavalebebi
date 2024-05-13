def sum_even_indices(numbers):
    """
    Calculate the sum of numbers at even indices in a list.

    Parameters:
    numbers (list of int): The list of integers.

    Returns:
    int: The sum of numbers at even indices.
    """
    sum_even = 0
    for i in range(0, len(numbers), 2):
        sum_even += numbers[i]
    return sum_even

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_indices(my_list)
print("Sum of numbers at even indices:", result)
#2 


def check_even_or_odd(number):
    """
    Check if a number is even or odd.

    Parameters:
    number (int): The number to be checked.

    Returns:
    str: 'Even' if the number is even, 'Odd' if the number is odd.
    """
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# Example usage:
result = check_even_or_odd(7)
print("Number is:", result)

#3

def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
#4

def capitalize_names(names):
    """
    Capitalize the first letter of each name in the list.

    Parameters:
    names (list of str): The list of names.

    Returns:
    list of str: The updated list where all names start with an uppercase letter.
    """
    capitalized_names = [name.capitalize() for name in names]
    return capitalized_names

# Example usage:
names_list = ["john", "emma", "michael", "sophia"]
updated_names = capitalize_names(names_list)
print("Updated names:", updated_names)

#5
def process_numbers(numbers):
    """
    Process numbers in a list: if the number is even, add number//2 to the new list,
    if it's odd, add number*2.

    Parameters:
    numbers (list of int): The list of integers.

    Returns:
    list of int: The updated list based on the processing rules.
    """
    processed_list = []
    for number in numbers:
        if number % 2 == 0:
            processed_list.append(number // 2)
        else:
            processed_list.append(number * 2)
    return processed_list

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
updated_list = process_numbers(numbers_list)
print("Updated list:", updated_list)