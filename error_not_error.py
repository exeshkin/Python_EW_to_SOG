'''
Перед запуском данной утилитки необходимо скопировать обрабатываемый
текст в файл 'error.txt' как есть.

После окончания работы данной утилитки отформатированный текст
будет сохранён в файле 'non_error.txt'. Данный текст подлежит
окончательной обработке вручную и сохранить его в соответствующий
файл исключения.
'''

import math


def splitting_line(line):
    '''
    Функция разбивает полученную строку на дополнительые строки,
    если длина исходной строки превышает 300 символов
        :param line : str Параграф в виде строки
        :return : str Параграф со строками длиной менее 300 символов
    '''
    # Заменить кавычки на обычные
    line = line.replace('“', '"')
    line = line.replace('”', '"')

    # Начало формирования параграфа
    final_line = ''
    # Определить длину параграфа
    length_line = len(line)

    # Проверить является ли длина параграфа больше 300 символов
    if length_line > 300:
        # Определить количество разделений параграфа
        count_broken_line = math.ceil(length_line / 300)
        # Определить длину строк разделений параграфа
        number_symb_broken_line = math.ceil(length_line / count_broken_line)

        # Начальный индекс разделителя
        index_witespace = 0
        for count in range(count_broken_line):
            count += 1
            if count == 1:
                # Определить индекс разделителя до первого пробела
                index_witespace = line.find(' ', number_symb_broken_line)
                # Обрезать параграф до индекса разделителя
                broken_line = line[:index_witespace + 1]
                # Добавить данные в параграф
                final_line += f'{broken_line}\n'
            else:
                # Определить предыдущий индекс разделителя
                prev_index_witespace = index_witespace + 1
                # Определить следующий индекс разделителя до первого пробела
                next_intermediate_index = index_witespace + number_symb_broken_line
                # Проверить является ли следующий индекс разделителя
                # больше длины параграфа
                if next_intermediate_index < length_line:
                    # Определить индекс разделителя до первого пробела
                    index_witespace = line.find(' ', next_intermediate_index)
                else:
                    # Определить индекс разделителя до конца параграфа
                    index_witespace = length_line
                # Обрезать параграф по индексам разделителя
                broken_line = line[prev_index_witespace:index_witespace + 1]
                # Добавить данные в параграф
                final_line += f'{broken_line}\n'
    else:
        # Добавить данные в параграф
        final_line = f'{line}\n'

    # Вернуть готовый параграф
    return final_line


def file_error():
    # Начало формирования текста
    new_text = ''

    # Открыть файл для чтения
    with open('error.txt', 'r', encoding='utf-8') as f:
        # Перебрать каждую строку текста
        for line in f:
            # Если строка непустая
            if line.strip() != '':
                # Обработать строку и вставить в текст
                new_text += splitting_line(line.strip())

    # Открыть файл для записи и вставить итоговый текст
    with open('non_error.txt', 'w', encoding='utf-8') as f:
        f.write(new_text)


# Проверка условия, импортирован ли модуль
if __name__ == '__main__':
    file_error()
