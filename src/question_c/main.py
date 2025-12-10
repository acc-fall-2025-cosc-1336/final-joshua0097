from question_c import get_most_likely_ancestor_consensus, validate_dna_string
def main():
    """Main program loop for finding DNA substring positions."""
    while True:
        print("\n=== DNA Substring Finder ===")
        
        # Get and validate main DNA string
        while True:
            dna_string1 = input("Enter a DNA string (greater than 8 and at most 16 characters): ").strip().upper()
            if validate_dna_string(dna_string1, min_length=8, max_length=16):
                break
            else:
                print("Invalid input! Please enter a DNA string with only A, C, G, T characters, greater than 8 and at most 16 characters long.")
        
        # Get and validate DNA substring
        while True:
            dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").strip().upper()
            if validate_dna_string(dna_string2, exact_length=4):
                break
            else:
                print("Invalid input! Please enter a DNA substring with only A, C, G, T characters, exactly 4 characters long.")
        
        # Call the function and get results
        results = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
        # Display results
        if results:
            print(f"\nSubstring '{dna_string2}' found at positions: {' '.join(map(str, results))}")
        else:
            print(f"\nSubstring '{dna_string2}' not found in '{dna_string1}'")
        
        # Ask if user wants to continue
        continue_choice = input("\nDo you want to search again? (yes/no): ").strip().lower()
        if continue_choice not in ['yes', 'y']:
            print("Goodbye!")
            break



if __name__ == "__main__":
    main()