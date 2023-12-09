def add(x, y):
    try:
        return x + y
    except TypeError as e:
        print(f"Exception: {e}")
        return


def sub(x, y):
    try:
        return x - y
    except TypeError as e:
        print(f"Exception: {e}")
        return


def mult(x, y):
    try:
        return x * y
    except TypeError as e:
        print(f"Exception: {e}")
        return


def div(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Zero Division Error")
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(f"Exception: {e}")
        return


while True:
    def to_float(num):
        while True:
            try:
                return float(input(num))
            except ValueError:
                print("Invalid , Enter a valid input:")


    num1 = to_float("\nEnter the first number: ")
    num2 = to_float("Enter the second number: ")
    op = input("Choose Operation to perform (+, -, *, /): ")
    print()

    if op in ('+', '-', '*', '/'):
        if op == '+':
            result = add(num1, num2)
            print(f'{num1} + {num2} = {result}' if result is not None else "Error occur")
        elif op == '-':
            result = sub(num1, num2)
            print(
                f'{num1} - {num2} = {result}' if result is not None else "Error occur")
        elif op == '*':
            result = mult(num1, num2)
            print(
                f'{num1} * {num2} = {result}' if result is not None else "Error occur")
        elif op == '/':
            result = div(num1, num2)
            print(f'{num1} / {num2} = {result}' if result is not None else "Error occur")
    else:
        print("Invalid operator,Enter a valid operator.")

    print('\n TO Continue')
    try:
        next_op = input(" 'y' for yes, 'n' for no: ")
        if next_op == 'n' or next_op != 'y':
            break
    except ValueError:
        print("Invalid option. Enter 'y' or 'n'.")

print("Goodbye!")
