# Task 4
#
# def reverse(input_str: str) -> str:
#     """
#     Function returns reversed input string
#     >>> reverse("hello") == "olleh"
#     True
#     >>> reverse("o") == "o"
#     True

def reverse(input_str: str) ->str:
    if len(input_str) == 1:
        return input_str
    return input_str[-1] + reverse(input_str[0:-1])


print(reverse("hello"))
input_word = input("Введите слово: ")
print(reverse(input_word))
