import vk


def main(search_param):
	session = vk.Session(access_token = 'bbb8c82cbbb8c82cbbb8c82c18bbd6ef60bbbb8bbb8c82ce6608e35886c40fa8a7df573')
	vk_api = vk.API(session)

	data = vk_api.photos.search(q = '#утро',
					 	lat = 55.753960,
					 	long = 37.620393,
					 	offset = 12,
					 	radius = 30000,
					 	v = 5.103)
	print(data)