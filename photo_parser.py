import vk
import json 
import requests


Yandex_Maps_Api_Key = "14e21f26-a134-47c4-b005-62081335b783"

def main(search_param):
	with open('districts.json', 'r', encoding='utf-8') as file:
		districts_list = json.load(file)
	# print(districts_list)
	session = vk.Session(access_token = 'bbb8c82cbbb8c82cbbb8c82c18bbd6ef60bbbb8bbb8c82ce6608e35886c40fa8a7df573')
	vk_api = vk.API(session)

	data = vk_api.photos.search(q = search_param,
					 	lat = 55.753960,
					 	long = 37.620393,
					 	offset = 100,
					 	radius = 20000,
					 	count = 100,
					 	v = 5.103)
	# print(data)
	# print(type(data))
	# data = json.loads(data)
	items = data['items']
	for item in items:
		item_lat = item['lat']
		item_long = item['long']
		# print(item_lat, item_long)


		

		request_text = "https://geocode-maps.yandex.ru/1.x/?"
		request_text += "apikey={}&geocode={},{}&format=json".format(Yandex_Maps_Api_Key,
														 item_long,
														 item_lat)
		# print(request_text)
		response = requests.get(request_text)
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
		try:
			if "район" in districts[-1]:
				name = districts[-1].split()
				name.pop(name.index('район'))
				# print(name[0])
				district_name = name[0]
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

	for district in districts_list:
		try:
			if districts_list[district][-1] != 0:
				print(district, districts_list[district][-1])
		except Exception:
			# print('EXCEPTED')
			continue

	# print(response.content.decode("utf-8"))
	print(len(items))