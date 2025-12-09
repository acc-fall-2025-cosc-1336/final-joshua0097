def create_multiplication_table():
    """
    Creates a multiplication table as a list of lists.
    
    Returns:
        list: A 2D list containing multiplication table values
    """
    # a - Create an empty list
    table = []
    
    # b - Use nested looping to create the table with lists
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            # Use multiplication to derive the values for each list element
            row.append(i * j)
        table.append(row)
    
    # c - return the list
    return table


def display_multiplication_table(table):
    """
    Displays a multiplication table from a 2D list.
    
    Args:
        table (list): A 2D list containing multiplication table values
    """
    # 1 - Loop through the list
    for row in table:
        # 2 - Display the table
        print("\t".join(str(value) for value in row))


if __name__ == "__main__":
    # Test the functions
    multiplication_table = create_multiplication_table()
    display_multiplication_table(multiplication_table)


