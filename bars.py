import json
import sys

def load_data(filepath):
	with open ( filepath[1] , 'r', encoding='windows-1251' ) as f:
		data = json.load(f)
		#print(data[0])
	return data


def get_biggest_bar(data):
	maxSeatsCount, index_biggest_bar = data[0]['SeatsCount'], 0
	for i in range(len(data)):
		if data[i]['SeatsCount'] > maxSeatsCount:
			maxSeatsCount = data[i]['SeatsCount']
			index_biggest_bar = i
	return data[index_biggest_bar]['Name']


def get_smallest_bar(data):
	minSeatsCount, index_smallest_bar = data[0]['SeatsCount'], 0

	for i in range(len(data)):
		if  data[i]['SeatsCount'] < minSeatsCount:
			minSeatsCount = data[i]['SeatsCount']
			index_smallest_bar = i

	return data[index_smallest_bar]['Name']



def get_closest_bar(data, longitude, latitude):
	x1, y1 = longitude, latitude
	x2, y2 = data[0]['geoData']['coordinates'][0], data[0]['geoData']['coordinates'][1]
	min_S = ( (x1-x2)**2 + (y1-y2)**2 )**0.5
	for i in range(len(data)):
		x2, y2 = data[i]['geoData']['coordinates'][0], data[i]['geoData']['coordinates'][1]
		if ( (x1-x2)**2 + (y1-y2)**2 )**0.5 < min_S:
			min_S = ( (x1-x2)**2 + (y1-y2)**2 )
			index_closest_bar = i
	return data[index_closest_bar]['Name']


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
