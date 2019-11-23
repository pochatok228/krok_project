from PIL import Image
import random

MOST_EAST_LONG = round(37.983968, 4)
MOST_WEST_LONG = round(37.295857, 4)
MOST_NORTH_LAT = round(55.964779, 4)
MOST_SOUTH_LAT = round(55.483864, 4)



Yandex_Maps_Api_Key = "14e21f26-a134-47c4-b005-62081335b783"
with open('districts.json', 'r', encoding='utf-8') as file:
		districts_list = json.load(file)
used_districts = {}

LONG_LEN = round(MOST_EAST_LONG - MOST_WEST_LONG, 4) * 10000
LONG_LAT = round(MOST_NORTH_LAT - MOST_SOUTH_LAT, 4) * 10000

print(LONG_LAT, LONG_LEN)

img = Image.new("RGB", (int(LONG_LAT), int(LONG_LEN)), (255, 255, 255))

img.show()
obj = img.load()

for smesh_len in range(int(LONG_LEN)):
	for smesh_lat in range(int(LONG_LAT)):

		item_long = MOST_WEAST_LONG + smesh_len / 10000
		item_lat = MOST_SOUTH_LAT + smesh_lat / 10000
		request_text = "https://geocode-maps.yandex.ru/1.x/?"
		request_text += "apikey={}&geocode={},{}&format=json".format(Yandex_Maps_Api_Key,
														 item_long,
														 item_lat)
		featureMember = response.json()['response']['GeoObjectCollection']['featureMember']
		for meta_object in featureMember:
			if 'район' in meta_object['GeoObject']['name']:
				raion = meta_object['GeoObject']['name']
				print(raion)
				districts = [raion]
		try:
			if "район" in districts[-1]:
				name = districts[-1].split()
				name.pop(name.index('район'))
				# print(name[0])
				district_name = ' '.join(name)
				if district_name in used_districts:
					pass
				else:
					while True:
						color = (random.randint(0, 256),
								 random.randint(0, 256),
								 random.randint(0, 256))
						if color in list(districts.values()):
							continue
						else:
							break
					used_districts[districts_name] = color
		img.putpixel()
