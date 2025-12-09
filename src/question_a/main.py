from question_a import create_multiplication_table, display_multiplication_table
def main():
    """
    Main function that runs the multiplication table program.
    """
    while True:
        # Create the multiplication table and save return values
        table_data = create_multiplication_table()
        
        # Display the multiplication table
        display_multiplication_table(table_data)
        
        # Ask user if they want to continue
        choice = input("\nDo you want to create another table? (yes/no): ").strip().lower()
        
        if choice in ['no', 'n', 'quit', 'exit']:
            print("Thank you for using the multiplication table program!")
            break


if __name__ == "__main__":
    main()