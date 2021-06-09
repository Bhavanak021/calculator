from art import logo
print(logo)
ans = True
while ans:
    num1 = float(input("What's the first number? "))
    print("+")
    print("-")
    print("*")
    print("/")
    operator = input("Pick an operator ")
    num2 = float(input("What's the next number? "))
    if operator == "+":
        cal = num1 + num2
    elif operator == "-":
        cal = num1 - num2
    elif operator == "*":
        cal = num1 * num2
    elif operator == "/":
        if num2 != 0:
            cal = num1 / num2
        else:
            print("Denominator 0 tends to infinity !!Invalid choice")
    else:
        print("Invalid operator")

    print(f"{num1} {operator} {num2} = {cal}")
    answ = input(f"Type 'y' if you want to continue calculation with {cal} ,or type 'n' if you want to"
            f" start a new calculation. ").lower()
    if answ == "y":
        ans = True
    else:
        ans = False
