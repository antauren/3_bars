import json
import sys
import os.path

def load_data(filepath):
    with open ( filepath , 'r', encoding='windows-1251' ) as f:
        return json.load(f)

def get_biggest_bar(bars_data):
    biggest_bar = max(bars_data, key=lambda bar: bar['SeatsCount'])
    return biggest_bar['Name']

def get_smallest_bar(bars_data):
    smallest_bar = min(bars_data, key=lambda bar: bar['SeatsCount'])
    return smallest_bar['Name']

def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min(bars_data, key = lambda bar:((longitude - bar['geoData']['coordinates'][0])**2 + (latitude - bar['geoData']['coordinates'][1])**2 )**0.5)
    return closest_bar['Name']

def get_coordinates(string):
    try:
        longitude, latitude = string.split()
        return [float(longitude), float(latitude)]
    except ValueError:
        print('Введите два числа(широта и долгота) через пробел: ')

        return get_coordinates( input() )


WELCOME = '''
Вас привествует программа поиска баров Москвы
Скрипт рассчитывает:
\t-самый большой бар
\t-самый маленький бар
\t-ближайший бар
Для того чтоб узнать как работает программа введите: python bars.py --help или python3 bars.py --help
'''

HELP = '''
Чтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <база_данных_json>
Наример: python3 bars.py data-2897-2016-11-23.json
Актуальную базу данных можно скачать с сайта открытых данных https://data.mos.ru/opendata/7710881420-bary
Файл базы данных нужно положить в папку, где находится скрипт bar.py
'''

ERROR = '''
Ошибка: программа не может найти файл с базой данных баров
Воспользуйтесь помощью (--help)
'''

PROGRAM_TEXT = '''
самый большой бар: {}
самый маленький бар: {}
для того чтобы узнать ближайший к Вам бар, введите gps-координаты (широта и долгота) через пробел:'''


def start_script(argv_list):
    if len(argv_list) < 2:
        print(WELCOME)
        return None

    filepath = argv_list[1]

    if filepath == '--help':
        print(HELP)
        return None

    if not os.path.exists(filepath):
        print (ERROR)        
        return None

    bars_data = load_data(filepath)
    print(PROGRAM_TEXT.format(get_biggest_bar(bars_data), get_smallest_bar(bars_data)))

    coordinates = get_coordinates(input())
    longitude, latitude = coordinates[0], coordinates[1]
    print('самый близкий бар:', get_closest_bar(bars_data, longitude, latitude))


if __name__ == '__main__':
    argv_list = sys.argv
    start_script(argv_list)