
# Task 2

# from typing import Optional
# def is_palindrome(looking_str: str, index: int = 0) -> bool:
#     """
#     Checks if input string is Palindrome
#     >>> is_palindrome('mom')
#     True
#
#     >>> is_palindrome('sassas')
#     True
#
#     >>> is_palindrome('o')
#     True
#     """
#     pass

def is_palindrome(looking_str: str, index: int = 0) ->bool:
    if len(looking_str) == 1 or len(looking_str) == 0:
        return True
    if looking_str[index] == looking_str[index-1]:
        return is_palindrome(looking_str[index+1:index-1])
    return False

print(is_palindrome('mom'))
print(is_palindrome('123321'))
print(is_palindrome('momy'))

