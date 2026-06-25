from bin_calc import (
    add_bin,
    sub_bin,
    mul_bin,
    div_bin,
    bin_to_dec,
    dec_to_bin,
)


def main():
    while True:
        print("\nWelcome to the Decimal-Binary Calculator!")
        print("Please choose an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Add two binary numbers")
        print("4. Subtract two binary numbers")
        print("5. Multiply two binary numbers")
        print("6. Divide two binary numbers")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        print()

        try:
            if choice == "1":
                dec_num = int(input("Enter a decimal number: "))
                binary_result = dec_to_bin(dec_num)
                print(f"The binary representation of {dec_num} is: {binary_result}")

            elif choice == "2":
                bin_num = input("Enter a binary number: ")
                decimal_result = bin_to_dec(bin_num)
                print(f"The decimal representation of {bin_num} is: {decimal_result}")

            elif choice in ["3", "4", "5", "6"]:
                num1 = input("Enter the first binary number: ")
                num2 = input("Enter the second binary number: ")

                if choice == "3":
                    print(f"Result: {add_bin(num1, num2)}")

                elif choice == "4":
                    print(f"Result: {sub_bin(num1, num2)}")

                elif choice == "5":
                    print(f"Result: {mul_bin(num1, num2)}")

                elif choice == "6":
                    quotient, remainder = div_bin(num1, num2)
                    print(f"Quotient : {quotient}")
                    print(f"Remainder: {remainder}")

            elif choice == "7":
                print("Thank you for using the Decimal-Binary Calculator! Goodbye!\n")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except ValueError as error:
            print(f"Input error: {error}")

        except ZeroDivisionError as error:
            print(f"Math error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()