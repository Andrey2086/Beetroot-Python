# Task 5
#
# def sum_of_digits(digit_string: str) -> int:
#     """
#     >>> sum_of_digits('26') == 8
#     True
#
#     >>> sum_of_digits('test')
#     ValueError("input string must be digit string")

def sum_of_digits(digit_string: str) -> int:
    if digit_string.isdigit() == False:
        raise ValueError("input string must be digit string")
    elif len(digit_string) == 1:
        return int(digit_string[0])
    else:
        summa = int(digit_string[0]) + int(sum_of_digits(digit_string[1:]))
        return sum_of_digits(str(summa))


assert  sum_of_digits('26') == 8
print(sum_of_digits('12345'))

