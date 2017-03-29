# -*- coding: utf-8 -*-
# coding: utf8

import json
import sys


hh = sys.argv

print(hh)
print(hh[0], hh[1])

with open ( hh[1], 'r', encoding='windows-1251' ) as f:
    data_again = json.load(f)

    maxSeatsCount, index_maxBar = data_again[0][ 'SeatsCount'], 0
    minSeatsCount, index_minBar = data_again[0]['SeatsCount'], 0

    def coordinates(i):
        try:
            x1, y1 = i.split()
            x1, y1 = float(x1), float(y1)
            return [x1, y1]
        except ValueError:
            #print('Че за фигню Вы там ввели???')
            print('Введите ДВА ЧИСЛА через ПРОБЕЛ: ')
            return coordinates( input() )

    print('Введите координаты (два числа через пробел): ')
    temp = coordinates(input())
    x1, y1 = temp[0], temp[1]

    x2 = data_again[0]['geoData']['coordinates'][0]
    y2 = data_again[0]['geoData']['coordinates'][1]

    nearBar_S = ( (x1-x2)**2 + (y1-y2)**2 )**0.5

    minBar = []

    for i in range(len(data_again)):
        if  data_again[i]['SeatsCount'] > maxSeatsCount:
            maxSeatsCount = data_again[i]['SeatsCount']
            index_maxBar = i

        if  data_again[i]['SeatsCount'] < minSeatsCount:
            minSeatsCount = data_again[i]['SeatsCount']
            index_minBar = i
            minBar = []
            minBar.append( data_again[index_minBar]['Name'] )

        else:
            if data_again[i]['SeatsCount'] == minSeatsCount:
                index_minBar = i
                minBar.append( data_again[index_minBar]['Name'] )

        x2 = data_again[i]['geoData']['coordinates'][0]
        y2 = data_again[i]['geoData']['coordinates'][1]

        if ( (x1-x2)**2 + (y1-y2)**2 )**0.5 < nearBar_S:
            nearBar_S = ( (x1-x2)**2 + (y1-y2)**2 )
            index_nearBar = i



    print('\nсамый близкий бар:', data_again[index_nearBar]['Name'])
    print('самый большой бар:', data_again[index_maxBar]['Name'])
    print('Число посадочных мест - ', data_again[index_maxBar]['SeatsCount'])

    minBAR = minBar[0]
    for i in range(1, len(minBar)):
        minBAR += ', ' + minBar[i]

    print('\nсамый маленький бар(ы):', minBAR, '\n',
          'Число посадочных мест - ', data_again[index_minBar]['SeatsCount'])

