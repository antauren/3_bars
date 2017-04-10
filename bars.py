import json
import sys

def load_data(filepath):
    with open ( filepath , 'r', encoding='windows-1251' ) as f:
        return json.load(f)

def get_biggest_bar(bars_data):
    biggest_bar = max((bar for bar in bars_data), key=lambda bar: bar['SeatsCount'])
    return biggest_bar['Name']

def get_smallest_bar(bars_data):
    smallest_bar = min((bar for bar in bars_data), key=lambda bar: bar['SeatsCount'])
    return smallest_bar['Name']

def get_closest_bar(bars_data, longitude, latitude):
    closest_bar = min((bar for bar in bars_data), key = lambda bar:((longitude - bar['geoData']['coordinates'][0])**2 + (latitude - bar['geoData']['coordinates'][1])**2 )**0.5)
    return closest_bar['Name']

def get_coordinates(string):
    try:
        longitude, latitude = string.split()
        return [float(longitude), float(latitude)]
    except ValueError:
        print('Введите два числа(широта и долгота) через пробел: ')

        return get_coordinates( input() )

def try_load_data(filepath):
    try:
        bars_data = load_data(filepath)
        print('самый большой бар: ', get_biggest_bar(bars_data))
        print('самый маленький бар:', get_smallest_bar(bars_data))
        print('для того чтобы узнать ближайший к Вам бар, введите gps-координаты (широта и долгота) через пробел: ')

        coordinates = get_coordinates(input())
        longitude, latitude = coordinates[0], coordinates[1]

        print('самый близкий бар:', get_closest_bar(bars_data, longitude, latitude))

    except FileNotFoundError:
        bars_data = None

    if bars_data is None:
        print('Ошибка: программа не может найти файл с базой данных баров')
        print('Воспользуйтесь помощью (--help)')

def try_get_filepath(argv_list):
    try:
        filepath = argv_list[1]

        if filepath == '--help':
            print('\nЧтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <база_данных_json>')
            print('Наример: python3 bars.py data-2897-2016-11-23.json\n')
            print('Актуальную базу данных можно скачать с сайта открытых данных https://data.mos.ru/opendata/7710881420-bary')
            print('Файл базы данных нужно положить в папку, где находится скрипт bar.py\n')

        else:
            try_load_data(filepath)
            

    except IndexError:
        filepath = None

    if filepath is None:
        print('Вас привествует программа поиска баров Москвы')
        print('Скрипт рассчитывает:')
        print('\t-самый большой бар')
        print('\t-самый маленький бар')
        print('\t-ближайший бар')
        print('Для того чтоб узнать как работает программа введите: python bars.py --help или python3 bars.py --help')
    
    return filepath


if __name__ == '__main__':
    argv_list = sys.argv
    try_get_filepath(argv_list)