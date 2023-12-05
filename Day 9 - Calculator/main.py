import Calculator

print("Welcome to the calculator")



while True:
    number_one=int(input("Give the first number: "))
    operation=input("Give the operation(/,*,+,-): ")
    number_two=int(input("Give the second number: "))

    if operation=='+':
        print(Calculator.addition(number_one,number_two))
    elif operation=='-':
        print(Calculator.subtraction(number_one,number_two))
    elif operation=='*':
        print(Calculator.multiplication(number_one,number_two))
    elif operation=='/':
        print(Calculator.division(number_one,number_two))
    else:
        print("Invalid operator given!!")

    option=input("Do you want to continue using the app?(Y/N)")
    if option=='N':
        break



