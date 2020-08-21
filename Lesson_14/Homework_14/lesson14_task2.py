    # Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

# def stop_words(words: list):
#      pass
#
# @stop_words(['pepsi', 'BMW'])
#
# def create_slogan(name: str) -> str:
#
#     return f"{name} drinks pepsi in his brand new BMW!"
#
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


def stop_words(words):
    def decorator(func):
        def wraper(name):
            str1 = func(name)
            for i in words:
                if i in func(name):
                    str1 = str1.replace(i, '*')
            return str1
        return wraper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Steve'))

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
