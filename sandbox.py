def named_function_decor(function_name):

    def function_decor(present_function):
        file = open(f'{function_name}.log', 'w', encoding='utf-8')

        def new_function(*args, **kwargs):

            result = present_function(*args, **kwargs)

            nonlocal file
            file.write(f'{function_name}({args}, {kwargs}) = {result}\n')

            return result

        # file.close()

        return new_function

    return function_decor
