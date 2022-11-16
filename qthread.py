from PyQt6.QtCore import QThread, pyqtSignal
import requests
import json
import os
import math
import re
import utils


class CreateSog(QThread):
    # Создать сигналы
    sig_except_one_line = pyqtSignal(str)
    sig_except_non_standard = pyqtSignal(str)
    sig_finish = pyqtSignal()
    sig_stop = pyqtSignal()

    # Инициализировать класса
    def __init__(self, mainwindow, parent=None):
        super(CreateSog, self).__init__(parent)
        # Принять параметр
        self.mainwindow = mainwindow

    def go(self):
        '''
        Функция получает список всех проповедей и на его основе
        создаёт файлы json для каждой проповеди
            :return: None
        '''

        # Начальный счетчик проповеди
        number = 1

        # Проверить есть ли файл. Если есть - удалить
        if os.path.isfile(f'finished_sog_file/{utils.name_file(self.mainwindow.combobox)}'):
            os.remove(
                f'finished_sog_file/{utils.name_file(self.mainwindow.combobox)}')
        # Удалить все файлы из папки
        utils.remove_files('temp_dwn_json')

        # Получить headers
        headers_list = utils.request_headers
        # Запросить данные с сервера
        response_list = requests.get(
            utils.request_url(self.mainwindow.combobox), params='meta=1', headers=headers_list)

        # Перевести строку в формат json
        data = json.loads(str(response_list.text))
        # Получить список проповедей
        list_sermons = data['1']['sermons']
        # Получить список ключей из словаря (из json)
        list_sermons_keys = list_sermons.keys()

        # Начальное значение итератора прогресс-бара
        value = 0

        # Перебрать все ключи
        for key in list_sermons_keys:
            # Если нажата кнопка "Стоп"
            if self.mainwindow.stop == True:
                break

            # Получить дополнительный параметр для ссылки на проповедь
            key_param = list(list_sermons[key].keys())

            # Запустить функцию для создания файла json
            self.article(headers_list, key, key_param[0])

            # Получить список всех файлов *.json из папки
            list_files_json = os.listdir('temp_dwn_json')
            # Получить список всех файлов *.excl из папки
            list_files_exclusion = os.listdir(
                utils.dir_exclusion(self.mainwindow.combobox))

            # Перебрать все файлы json в папке
            for file in list_files_json:
                # Пеменная с именем файла *.excl
                name_file = f'{file[:-5]}.excl'

                # Проверить есть ли в исключениях файл *.excl
                if name_file in list_files_exclusion:
                    # Удалить файл json
                    os.remove(f'temp_dwn_json/{file}')
                else:
                    # Запустить функцию для создания файла sog
                    self.create_file_sog(number)
                    number += 1

            # Увеличение значения итератора прогресс-бара
            value += 1
            # Вычисление значения прогресс-бара
            current_value_progress_bar = value * 100 / len(list_sermons_keys)
            # Установка значения прогресс-бара
            self.mainwindow.ui.progress_bar.setValue(
                int(current_value_progress_bar))

        # Если нажата кнопка "Стоп"
        if self.mainwindow.stop:
            # Послать сигнал
            self.sig_stop.emit()
        else:
            # Запустить функцию для добавления исключений в файл sog
            self.insert_exceptions_in_sog(number)
            # Послать сигнал
            self.sig_finish.emit()

    def splitting_line(self, line):
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
            number_symb_broken_line = math.ceil(
                length_line / count_broken_line)

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
                        index_witespace = line.find(
                            ' ', next_intermediate_index)
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

    def create_file_sog(self, number):
        '''
        Функция создаёт файл *.sog из файлов *.json
            :param number : int Порядковый номер добавляемой проповеди
            :return : None
        '''
        # Получить список всех файлов *.json из папки
        list_files_json = os.listdir('temp_dwn_json')

        # Задать пустые переменные для сигналов
        warn_one_line = ''
        warn_non_standard = ''

        # Перебрать все файлы json в папке
        for file in list_files_json:
            try:
                # Определить дату файла
                date = file

                # Открыть файл json для чтения
                with open(f'temp_dwn_json/{file}', 'r', encoding='utf-8') as f:
                    # Получить данные файла в формате json
                    file_json = json.load(f)

                    # Начало формирования проповеди
                    current_sermon = ''

                    # Добавить номер в содержимое файла
                    current_sermon += f'{utils.number_str(number)}\n'

                    # Добавить название, дату, место проповеди и перевод в содержимое файла
                    current_sermon += f'{file_json["title"].upper()} {date[:-5]} — {file_json["location"]}\n'

                    # Получить все ключи из исходного файла
                    keys_file_json = list(file_json.keys())
                    # Список ключей для удаления
                    list_keys_remove = utils.keys_for_remove(
                        self.mainwindow.combobox)
                    # Удалить ключи из списка
                    for key_del in list_keys_remove:
                        keys_file_json.remove(key_del)

                    # Заменить все ключи из str в int
                    for ind, value in enumerate(keys_file_json):
                        # Если имеется подчеркивание, то заменить на '.'
                        if '_' in value:
                            keys_file_json[ind] = float(
                                value.replace('_', '.'))
                        else:
                            keys_file_json[ind] = int(value)

                    # Отсортировать список
                    keys_file_json.sort()

                    # Перебрать каждую строку и записать в файл в нужном формате
                    for line in keys_file_json:
                        # Заменить все ключи из int в str
                        if '.' in str(line):
                            str_line = str(line).replace('.', '_')
                        else:
                            str_line = str(line)

                        # Добавить номер строки и отформатированную строку в содержимое файла
                        current_sermon += f'{line}. {self.splitting_line(file_json[str_line])}'

                    # Открыть файл sog для добавления проповедей
                    with open(f'finished_sog_file/{utils.name_file(self.mainwindow.combobox)}', 'a', encoding='utf-8') as f:
                        if len(keys_file_json) != 1:
                            # Записать отформатированную проповедь в файл sog
                            f.write(str(f'{current_sermon}\n'))
                        else:
                            # Присвоить переменной имя файла для сигнала
                            warn_one_line = file

                # Удалить обработанный файл
                os.remove(f'temp_dwn_json/{file}')
            except:
                # Удалить обработанный файл
                os.remove(f'temp_dwn_json/{file}')

                # Присвоить переменной имя файла для сигнала
                warn_non_standard = file

        # Отослать сигнал об ошибке
        if warn_one_line:
            self.sig_except_one_line.emit(warn_one_line)

        # Отослать сигнал об ошибке
        if warn_non_standard:
            self.sig_except_non_standard.emit(warn_non_standard)

    def article(self, headers, date_time, additional_param):
        '''
        Функция создаёт файлы json для каждой проповеди на основании запроса
            :param headers : str Для создания запроса на сервер
            :param date_time : str Дата проповеди для формирования ссылки на запрос данных
            :param additional_param : str Доп. параметр для формирования ссылки на запрос данных
            :return: None
        '''
        head = headers
        date = date_time
        param = additional_param

        # Начало формирования содержимого файла
        article_json = '{'

        # Запросить данные (название, место, ...) по определенной статье
        response_titles = requests.get(
            f'{utils.request_url(self.mainwindow.combobox)}/1/{date}', headers=head)
        # Получить текст из запроса и обрезать ненужные символы
        title_text = (response_titles.text)[2:-2]
        # Добавить данные в содержимое файла
        article_json += f'{title_text},'

        # Запросить данные (текст проповеди) по определенной статье
        response_content_article = requests.get(
            f'{utils.request_url(self.mainwindow.combobox)}/1/{date}/{param}', headers=head)
        # Получить текст из запроса
        data_text = response_content_article.text

        # Перевести строку в формат json
        data_json_content = json.loads(data_text)

        # Форматирование каждой строки в нужный вид
        for item in data_json_content:
            # Заменить все одинарные кавычки на двойные
            num = str(item['number']).replace('"', "'")
            text = str(item['text']).replace('"', "'")
            # Удалить перносы строк
            for _ in range(5):
                text = text.replace('\n', ' ')
                text = text.replace('\r', ' ')
            # Удалить все теги из строки
            text = re.sub(r'\<[^>]*\>', '', text)
            # Удалить '\'
            text = text.replace('\\', ' ')

            # Найти первый пробел в строке
            index_whitespace = text.find(' ')
            # Удалить номер и пробел из начала строки
            text = text[index_whitespace + 1:]

            # Добавить данные (номер параграфа и текст) в содержимое файла
            article_json += f'"{num}":"{text}",'
        # Удалить последнюю запятую из содержимого файла
        article_json = article_json[:-1]
        # Окончание формирования содержимого файла
        article_json += '}'

        # Запись содержимого в файл JSON с соответсвующим названием (датой проповеди)
        with open(f'temp_dwn_json/{date}.json', 'w', encoding='utf-8') as file:
            file.write(str(article_json))

    def insert_exceptions_in_sog(self, number):
        '''
        Функция дополняет файл *.sog из файлов *.excl
            :param number : int Порядковый номер добавляемой проповеди
            :return : None
        '''
        # Номер текущей проповеди
        number_excl = number
        # Получить список файлов исключений
        list_files_exclusion = os.listdir(
            utils.dir_exclusion(self.mainwindow.combobox))

        # Переменная для счета количества строк в проповеди
        count_line = 0

        # Добавить содержимое каждого файла в файл sog
        for file_excl in list_files_exclusion:
            # Содержание текущей проповеди
            sermon_exclusion = ''

            # Открыть файл исключения
            with open(f'{utils.dir_exclusion(self.mainwindow.combobox)}/{file_excl}', 'r', encoding='utf-8') as f:
                # Посчитать количество строк
                count_line = sum(1 for _ in f)

            # Если количество строк в проповеди больше 5
            if count_line > 5:
                # Открыть файл исключения
                with open(f'{utils.dir_exclusion(self.mainwindow.combobox)}/{file_excl}', 'r', encoding='utf-8') as f:
                    # Добавить номер проповеди в содержание текущей проповеди
                    sermon_exclusion += f'{utils.number_str(number_excl)}\n'
                    # Вставить текст проповеди
                    sermon_exclusion += f.read()

                # Открыть файл sog
                with open(f'finished_sog_file/{utils.name_file(self.mainwindow.combobox)}', 'a', encoding='utf-8') as f:
                    # Добавить в файл текущую проповедь
                    f.write(str(f'{sermon_exclusion}\n'))

                # Итерировать номер текущей проповеди
                number_excl += 1

    def run(self):
        # Старт
        self.go()
