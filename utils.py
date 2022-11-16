'''
Вспомогательные переменные и функции
'''

import os

# Заголовки запроса
request_headers = {
    'authority': 'cloud.eternalwords.net',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'origin': 'https://reader.eternalwords.net',
    'referer': 'https://reader.eternalwords.net/',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
}

# Ссылка на запрос
request_url_link = 'https://cloud.eternalwords.net/ext/readeronline'


def request_url(cb_item):
    '''
    Функция принимает значение QComboBox и возвращает ссылку на запрос
        :param cb_item : str значение QComboBox
        :return : str Cсылка на запрос
    '''

    if cb_item == 'cb_message':
        url = f'{request_url_link}/message'

    if cb_item == 'cb_vin':
        url = f'{request_url_link}/tea'

    return url


def keys_for_remove(cb_item):
    '''
    Функция принимает значение QComboBox и возвращает список ключей
        :param cb_item : str значение QComboBox
        :return : list Список ключей
    '''

    if cb_item == 'cb_message':
        list = ['id', 'translation', 'title',
                'subtitle', 'series', 'location', 'audiourl']

    if cb_item == 'cb_vin':
        list = ['id', 'translation', 'title', 'subtitle', 'series',
                'location', 'audiourl', 'videourl', 'skip_time']

    return list


def name_file(cb_item):
    '''
    Функция принимает значение QComboBox и возвращает название файла
        :param cb_item : str значение QComboBox
        :return : str Название файла
    '''

    if cb_item == 'cb_message':
        name = 'Послание_EW.sog'

    if cb_item == 'cb_vin':
        name = 'Вин_EW.sog'

    return name


def dir_exclusion(cb_item):
    '''
    Функция принимает значение QComboBox и возвращает ссылку на папку с исключениями
        :param cb_item : str значение QComboBox
        :return : str Cсылка на папку с исключениями
    '''

    if cb_item == 'cb_message':
        dir = 'exclusion_message'

    if cb_item == 'cb_vin':
        dir = 'exclusion_vin'

    return dir


def number_str(number):
    '''
    Функция принимает число и возвращает строку
        :param number : int Число
        :return : str Строка
    '''

    # Строка формируется в зависимости от количества цифр в числе
    match len(str(number)):
        case 1:
            number = f'000{number}'
        case 2:
            number = f'00{number}'
        case 3:
            number = f'0{number}'
    return number


def remove_files(dir):
    '''
    Функция принимает ссылку на папку и очищает её содержимое
        :param dir : str Ccылкf на папку
        :return : None
    '''

    try:
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    except:
        pass


# Текст окна с информацией
info_text = '''Данная утилита предназначена для сборки файлов '.sog'
с проповедями Уилльяма Марриона Бранхама и Вина Даяла.
Файлы '.sog' используются в программе 'SongOfGod', которую можно
скачать с сайта www.songofgod.ru.
-------------------------------------------------------------------
Файлы формируются из открытого ресурса reader.eternalwords.net.
Соответственно, для работы утилиты нужен включенный интернет.
По состоянию на ноябрь 2022 года утилита работает исправно.
-------------------------------------------------------------------
Если в процессе сборки появится сообщение, что проповедь
в файл sog НЕ добавлена, то необходимо добавить эту проповедь
в папку исключений самостоятельно.
Файлы исключений находятся в папках:
- Уилльяма Марриона Бранхама - в папке 'exclusion_message'
- Вина Даяла - в папке 'exclusion_vin'
Текущие файлы исключений в этих папках уже есть.
-------------------------------------------------------------------
По завершению сборки, готовый файл будет находится
в папке 'finished_sog_file'
'''
