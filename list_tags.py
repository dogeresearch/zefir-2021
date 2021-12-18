import json
from os import path

json_file = 'tag_data.json'

with open(json_file, 'r') as f:
    photos_data = json.load(f)

tag_length = []

for tag, photos in photos_data['tag_to_id'].items():
    tag_length.append((len(photos), tag))

tag_length = sorted(tag_length)[::-1]

print('All tags:')
for length, tag in tag_length:
    print(f'{tag}: {length} photos')