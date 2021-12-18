import json

json_file = 'tag_data.json'

with open(json_file, 'r') as f:
    photos_data = json.load(f)

tag_to_find = input('Tag: ')

if tag_to_find not in photos_data['tag_to_id']:
    print('No photos found :(')
    exit(0)

prob_link = []

for pid, prob in photos_data['tag_to_id'][tag_to_find]:
    prob = float(prob)
    path, link = photos_data['id_to_data'][str(pid)]
    prob_link.append((prob, link))

prob_link = sorted(prob_link)[::-1]

for prob, link in prob_link:
    print(f'{link}\t{prob}')