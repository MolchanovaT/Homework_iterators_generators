from functools import wraps
import datetime


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        # действия до вызова исходной функции
        start = datetime.datetime.now()

        result = old_function(*args, **kwargs)

        lines = [f'Дата и время запуска функции {start}', f'Имя функции {old_function.__name__}',
                 f'Аргументы {args}  {kwargs}',
                 f'Функция возвращает {result}']

        with open("main.log", "a", encoding="utf-8") as file:
            for line in lines:
                file.write(line + '\n')

        return result

    return new_function
