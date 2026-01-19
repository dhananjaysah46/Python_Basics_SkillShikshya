# Assignment-2 Day-3: A python program to calculate and store the sum, difference, multiplication, division of a list of numbers seperately

# Initializing separate lists for storage
sum_list = []
difference_list = []
multiplication_list = []
division_list = []

def calculate():
    while True:
        # Displaying Options using escape characters for better readability
        print("\nPython Calculator Menu:-")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit & View History")
        
        choice = input("\nSelect an operation (1-5): ")

        if choice == '5':
            print("\nExiting... Here is your history:")
            break
            
        # Escape characters used for clean formatting
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("\tEnter first number: "))
            num2 = float(input("\tEnter second number: "))

            # Nested logic: Choice-based operations
            if choice == '1':
                result = num1 + num2
                sum_list.append(result)
                print(f"Result: {result} added to sum_list.")
                
            elif choice == '2':
                result = num1 - num2
                difference_list.append(result)
                print(f"Result: {result} added to difference_list.")
                
            elif choice == '3':
                result = num1 * num2
                multiplication_list.append(result)
                print(f"Result: {result} added to multiplication_list.")
                
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    division_list.append(result)
                    print(f"Result: {result} added to division_list.")
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice, please try again.")

calculate()

# Displaying the final lists
print(f"\nFinal Records:\nSums: {sum_list}\nDiffs: {difference_list}\nMuls: {multiplication_list}\nDivs: {division_list}")


