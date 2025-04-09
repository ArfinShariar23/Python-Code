def calculator():
    while True:
        print("Welcome to the Simple Calculator score")
        #input number1
        num1 = int(input("Enter Number 1: "))
        #input number2
        num2 = int(input("Enter Number 2: "))

        #Input Operation
        operation = input("Please Choose your Operation (+/-/x/%//): ")

        if operation=="+":
            sum = num1+num2
            print(f"{num1}+{num2}={sum}")
        elif operation=="-":
            if num1>num2:
                sub = num1-num2
                print(f"{num1}-{num2}={sub}")
            else:
                sub = num2-num1
                print(f"{num2}-{num1}={sub}")
        elif operation == "x":
            mul = num1*num2
            print(f"{num1}x{num2}={mul}")
        elif operation == "/":
            if num1>num2:
                div = num1/num2
                print(f"{num1}/{num2}={div}")
            else:
                div = num2/num2
                print(f"{num2}/{num1}={div}")
        elif operation == "%":
            mod = num1%num2
            print(f"{num1}%{num2}={mod}")
        else:
            print("Invalid Input")
calculator()