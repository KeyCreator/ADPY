import json

file = open(f'phones.json', 'w')
data = ('Sergey', 'Klimov', '952', True)
contact = [[data]]
json.dump(contact, file)
file.close()