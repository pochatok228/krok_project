import vk
import json 
import requests


Yandex_Maps_Api_Key = "14e21f26-a134-47c4-b005-62081335b783"

def main(search_param, offset, used_photos):
	with open('districts.json', 'r', encoding='utf-8') as file:
		districts_list = json.load(file)
	# print(districts_list)
	session = vk.Session(access_token = 'bbb8c82cbbb8c82cbbb8c82c18bbd6ef60bbbb8bbb8c82ce6608e35886c40fa8a7df573')
	vk_api = vk.API(session)

	data = vk_api.photos.search(q = search_param,
					 	lat = 55.753960,
					 	long = 37.620393,
					 	offset = 50,
					 	radius = 1000,
					 	count = 1000,
					 	v = 5.103)
	# print(data)
	# print(type(data))
	# data = json.loads(data)
	array_for_return = []
	items = data['items']
	counter = 0
	# print(data)
	# with open('data.json', 'w') as file:
	# 	json.dump(data, file)
	for item in items:
		# print(item)
		try:
			item_lat = item['lat']
			item_long = item['long']
			if item['id'] in used_photos:
				continue
			else:
				# print("Found Deda")
				used_photos.append(item['id'])

				# print(item_lat, item_long )
				if item['sizes'] != []:
					url = item['sizes'][-1]["url"]
				else:
					url = 'None'
				array_for_return.append({"url": url, "lat": item_lat, "long": item_long})
		
		except Exception as e:
			print(e)
		

		# print(item_lat, item_long)


		"""
		request_text = "https://geocode-maps.yandex.ru/1.x/?"
		request_text += "apikey={}&geocode={},{}&format=json".format(Yandex_Maps_Api_Key,
														 item_long,
														 item_lat)
		print(request_text)
		response = requests.get(request_text)
		# print(response)
		
		try:
			meta = response.json()['response']['GeoObjectCollection']['featureMember'][-6]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
			# print(response['GeoObjectCollection']['featureMember']['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
			# print(meta)
			districts = []
			for component in meta:
				component_kind = component['kind']
				if component_kind == 'district':
					districts.append(component['name'])
		except Exception:
			meta = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
			# print(response['GeoObjectCollection']['featureMember']['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
			# print(meta)
			for component in meta:
				component_kind = component['kind']
				if component_kind == 'district':
					districts.append(component['name'])
					
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
				if district_name in districts_list:
					
					if districts_list[district_name] != []:
						districts_list[district_name][-1] += 1
					else:
						districts_list[district_name].append(1)
					
					# print('FOUND',
					# district_list, districts_list[district_name]
					# )
					# print(district_name, districts_list[district_name])
		except Exception:
			pass

	array_for_return = []
	for district in districts_list:
		try:
			if districts_list[district][-1] != 0:
				print(district, districts_list[district][-1])
				array_for_return.append((district, districts_list[district][-1]))
		except Exception:
			# print('EXCEPTED')
			continue

	# print(response.content.decode("utf-8"))
	# print(len(items))
	print(array_for_return)
	"""

	# print(array_for_return, used_photos)
	return array_for_return, used_photos
