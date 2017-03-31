import json
import sys

def load_data(filepath):
    with open ( filepath[1] , 'r', encoding='windows-1251' ) as f:
        return json.load(f)

def get_biggest_bar(data):
    max_seats_count, biggest_bar = data[0]['SeatsCount'], data[0]
    for bar in data:
        if bar['SeatsCount'] > max_seats_count:
            max_seats_count = bar['SeatsCount']
            biggest_bar = bar
    return biggest_bar['Name']


def get_smallest_bar(data):
    min_seats_count, smallest_bar = data[0]['SeatsCount'], data[0]
    for bar in data:
        if  bar['SeatsCount'] < min_seats_count:
            min_seats_count = bar['SeatsCount']
            smallest_bar = bar
    return smallest_bar['Name']

def get_closest_bar(data, longitude, latitude):
    closest_bar = data[0]
    x1, y1 = longitude, latitude
    x2, y2 = data[0]['geoData']['coordinates'][0], data[0]['geoData']['coordinates'][1]
    min_distance = ( (x1-x2)**2 + (y1-y2)**2 )**0.5

    for bar in data:
        x2, y2 = bar['geoData']['coordinates'][0], bar['geoData']['coordinates'][1]
        if ( (x1-x2)**2 + (y1-y2)**2 )**0.5 < min_distance:
            min_distance = ( (x1-x2)**2 + (y1-y2)**2 )
            closest_bar = bar
    return closest_bar['Name']


def get_coordinates(string):
    try:
        x1, y1 = string.split()
        x1, y1 = float(x1), float(y1)
        return [x1, y1]
    except ValueError:
        print('Введите ДВА ЧИСЛА через ПРОБЕЛ: ')
        return get_coordinates( input() )

filepath = sys.argv
data = load_data(filepath)

print('самый большой бар: ', get_biggest_bar(data))
print('самый маленький бар:', get_smallest_bar(data))
print('для того чтобы узнать ближайший к Вам бар, введите координаты (два числа через пробел): ')

temp = get_coordinates(input())
longitude, latitude = temp[0], temp[1]

print('самый близкий бар:', get_closest_bar(data, longitude, latitude))


if __name__ == '__main__':
    pass