import json
import sys

filepath = sys.argv
print(filepath)


def load_data(filepath):
	with open ( filepath[1] , 'r', encoding='windows-1251' ) as f:
		data = json.load(f)
		print(data)


def get_biggest_bar(data):


    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


print(load_data(filepath))


if __name__ == '__main__':
    pass
