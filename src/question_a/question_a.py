#write functions here, don't add input('') statements here!

def create_multiplication_table():
    """
    Creates a multiplication table based on user input.
    Returns a tuple of (number, range) or None if invalid input.
    """
    try:
        number = int(input("Enter a number for the multiplication table: "))
        table_range = int(input("Enter the range for the table: "))
        return (number, table_range)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None

def display_multiplication_table(table_data):
    """
    Displays a multiplication table based on the provided data.
    
    Args:
        table_data: A tuple containing (number, range)
    """
    if table_data is None:
        return
    
    number, table_range = table_data
    print(f"\nMultiplication Table for {number}:")
    print("-" * 30)
    for i in range(1, table_range + 1):
        result = number * i
        print(f"{number} x {i} = {result}")
    print("-" * 30)