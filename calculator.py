# !/user/bin/env.python3
# Created By: Peter Sobowale
# Date: Dec 1, 2022
# This program asks user for 2 numbers and a symbol and
# calculates accordingly like a calculator


def calculate(operation, first_number, second_number):
    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "/":
        answer = first_number / second_number
    elif operation == "%":
        answer = first_number % second_number
    return answer


def main():

    # asks user for the operator that they want to use
    user_operation = input(
        "Enter the operator that you would like to use in your calculation(+, -, *, /, %): "
    )

    if (
        user_operation == "+"
        or user_operation == "-"
        or user_operation == "*"
        or user_operation == "/"
        or user_operation == "%"
    ):
        # asks user for the first number that they want to use in their operation
        first_number_string = input("Enter your first number here: ")
        try:
            first_number_float = float(first_number_string)

            # asks user for the second number that they want to use in their equation
            second_number_string = input("Enter your second number here: ")
            try:
                second_number_float = float(second_number_string)

                # assigns variable to function call that gives return value
                solution_user = calculate(
                    user_operation, first_number_float, second_number_float
                )
                print(
                    "The result of {} {} {} = {:.2f}".format(
                        first_number_float,
                        user_operation,
                        second_number_float,
                        solution_user,
                    )
                )
            # catches any invalid input
            except Exception:
                print("{} is not a valid number. ".format(second_number_string))
        # catches any invalid input
        except Exception:
            print("{} is not a valid number.".format(first_number_string))
    # catches any invalid input
    else:
        print("{} is not a valid operator".format(user_operation))


if __name__ == "__main__":
    main()
