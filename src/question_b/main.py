from question_b import get_stock_list, display_stock_list

def main():
    stock_list = get_stock_list()
    
    while True:
        print("\n1-Display stock purchase history")
        print("2-Exit")
        choice = input("\nEnter option: ")
        
        if choice == '1':
            display_stock_list(stock_list)
        elif choice == '2':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
 

