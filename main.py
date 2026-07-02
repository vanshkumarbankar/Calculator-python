while True:  # for running loop
    Num1 = float(input('Enter Your First Number: '))  # ask the first number
    Num2 = float(input('Enter Your Second Number: '))  # ask the second number

    print("Available operators: +  -  *  /  //  %  **")
    operator = input('Enter Your Operator: ')  # ask for the operator

    if operator == '+':
        print(f"{Num1}+{Num2}={Num1 + Num2}")

    elif operator == '-':
        print(f"{Num1}-{Num2}={Num1 - Num2}")

    elif operator == '*':
        print(f"{Num1}*{Num2}={Num1 * Num2}")

    elif operator == '/':
        if Num2 == 0:
            print("Division by 0 is not allowed")
        else:
            print(f"{Num1}/{Num2}={Num1 / Num2}")

    elif operator == '%':
        if Num2 == 0:
            print("Division by 0 is not allowed")
        else:
            print(f"{Num1}%{Num2}={Num1 % Num2}")

    elif operator == '**':
        print(f"{Num1}**{Num2}={Num1 ** Num2}")

    elif operator == '//':
        if Num2 == 0:
            print("Division by 0 is not allowed")
        else:
            print(f"{Num1}//{Num2}={Num1 // Num2}")

    else:
        print("Invalid operator. Please choose one of the available operators.")

    x = input('Do you want to continue? (y/n): ').lower()

    if x != 'y':
        print("Thank you for using the calculator!")
        print("Calculator closed.")
        break
