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

def start_script(argv_list):
    if len(argv_list) < 2:
        print('Вас привествует программа поиска баров Москвы'
              'Скрипт рассчитывает:\n'
              '\t-самый большой бар\n'
              '\t-самый маленький бар\n'
              '\t-ближайший бар\n'
              'Для того чтоб узнать как работает программа введите: python bars.py --help или python3 bars.py --help')
        return None

    filepath = argv_list[1]

    if filepath == '--help':
        print('Чтобы запустить программу, нужно ввести в консоли: <интерпретатор> <скрипт> <база_данных_json>\n'
              'Наример: python3 bars.py data-2897-2016-11-23.json\n'
              'Актуальную базу данных можно скачать с сайта открытых данных https://data.mos.ru/opendata/7710881420-bary\n'
              'Файл базы данных нужно положить в папку, где находится скрипт bar.py')
        return None

    if not os.path.exists(filepath):
        print('Ошибка: программа не может найти файл с базой данных баров\n'
              'Воспользуйтесь помощью (--help)')
        return None

    bars_data = load_data(filepath)
    print('самый большой бар: {}\n'
          'самый маленький бар: {}\n'
          'для того чтобы узнать ближайший к Вам бар, введите gps-координаты (широта и долгота) через пробел:'
          .format(get_biggest_bar(bars_data), get_smallest_bar(bars_data)))

    coordinates = get_coordinates(input())
    longitude, latitude = coordinates[0], coordinates[1]
    print('самый близкий бар:', get_closest_bar(bars_data, longitude, latitude))


if __name__ == '__main__':
    argv_list = sys.argv
    start_script(argv_list)