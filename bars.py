import json
import sys

def load_data(filepath):
    with open ( filepath[1] , 'r', encoding='windows-1251' ) as f:
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
        print('Введите ДВА ЧИСЛА(широта и долгота) через ПРОБЕЛ: ')
        return get_coordinates( input() )

filepath = sys.argv
bars_data = load_data(filepath)

print('самый большой бар: ', get_biggest_bar(bars_data))
print('самый маленький бар:', get_smallest_bar(bars_data))
print('для того чтобы узнать ближайший к Вам бар, введите координаты (два числа через пробел): ')

coordinates = get_coordinates(input())
longitude, latitude = coordinates[0], coordinates[1]

print('самый близкий бар:', get_closest_bar(bars_data, longitude, latitude))

if __name__ == '__main__':
    pass