import sys

operator_check = ("+", "-", "*", "/")
float_check = "."


#  Questions closed in functions, each catch letter exception


def first_question():
    while True:
        try:
            number_a = enter_first_number_txt()
            break
        except ValueError:
            user_exit()
    return number_a


def second_question():
    while True:
        try:
            mark = enter_operation_mark()
            return mark
        except ValueError:
            user_exit()
    return mark


def third_question():
    while True:
        try:
            number_b = enter_next_number_txt()
            break
        except ValueError:
            third_question()  # not working
    return number_b


# Collect numbers and mark, functions


def enter_first_number_txt():
    number_a = int(input('Enter a number (or a letter to ' + '\033[1m' + 'exit' + '\033[0m' + ') '))
    check_float = str(number_a)
    while float_check in check_float: # Not working
        print("Integers only, please")
        return first_question()

    return number_a


def enter_operation_mark():
    mark = str(input('Enter an operation: '))
    while mark not in operator_check: # same but works just fine
        print('pick from "+", "-", "*", "/"')
        return second_question()
    return mark


def enter_next_number_txt():
    number_b = int(input('Enter another number: '))
    return number_b


def user_exit():
    print("Downloading your naked pics.. now, you may go. Bye!")
    sys.exit(0)


# Check marks and count


def answer(number_a, number_b, mark):
    pick_from_answer = 'pick from "+", "-", "*", "/"'
    do_not_divide_by_zero = 'Next time you should not divide by 0'

    if mark == "+":
        answer = number_a + number_b
        return answer
    elif mark == "-":
        answer = number_a - number_b
        return answer
    elif mark == "*":
        answer = number_a * number_b
        return answer
    elif mark == "/":

        if number_b == 0:
            print(do_not_divide_by_zero)
            return third_question()
        else:
            answer = number_a / number_b
        return answer

    else:
        return pick_from_answer


# Main function starting program definition


def main():
    number_a = first_question()
    mark = second_question()
    number_b = third_question()
    print('Result: ' + str(answer(number_a, number_b, mark)) + '\n')
    main()


# Calling main function, starts the program

if __name__ == '__main__':
    main()
