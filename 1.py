import json
with open ('data-2897-2016-11-23.json', 'r', encoding='windows-1251') as f:   #(hh[1], 'r') as f:
    data = json.load(f)  # .decode('utf-8')
print (data)