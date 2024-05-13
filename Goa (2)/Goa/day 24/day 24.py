def calculate_area_of_rectangle(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

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

def generate_fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence up to n terms.

    Parameters:
    n (int): The number of terms in the Fibonacci sequence.

    Returns:
    list: The Fibonacci sequence.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

# Example usage of the functions
print("Area of rectangle:", calculate_area_of_rectangle(5, 4))
print("Even or Odd:", check_even_or_odd(7))
print("Fibonacci sequence:", generate_fibonacci_sequence(10))