import sys


def adv_print(*args, **kwargs):
    ''' adv_print - расширение базовой функции print

    Добавлены следующие именованные аргументы
    start - с чего начинается вывод. По умолчанию пустая строка
    max_line - максимальная длин строки при выводе. Если строка превышает max_line, то вывод автоматически переносится на новую строку
    in_file - логическое значение. Если True, то вывод на экран и в файл adv_print.txt
    '''

    ' Обрабатываем "родные" параметры '
    sep = kwargs['sep'] if 'sep' in kwargs.keys() else ' '
    end = kwargs['end'] if 'end' in kwargs.keys() else '\n'
    file = kwargs['file'] if 'file' in kwargs.keys() else sys.stdout
    flush = kwargs['flush'] if 'flush' in kwargs.keys() else False

    ' Обрабатываем дополнительные параметры '
    start = kwargs['start'] if 'start' in kwargs.keys() else '\n'
    max_line = kwargs['max_line'] if 'max_line' in kwargs.keys() else 0
    in_file = kwargs['in_file'] if 'in_file' in kwargs.keys() else False

    str_out = f'{start}{sep.join(args)}'

    if max_line:
        str_out = [str_out[x: x + max_line] for x in range(0, len(str_out), max_line)]
        str_out = '\n'.join(str_out)

    if in_file:
        file_out = open('adv_print.txt', 'w')
        file_out.write(str_out)
        file_out.close()

    print(str_out, end=end, file=file, flush=flush)


if __name__ == "__main__":
    adv_print('Barnaul - the capital of the world', max_line=8, in_file=True)