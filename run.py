import photo_parser
import drawer
import json


phrase = input()

main_stats = []
data_array = []
used_photos = []
search_words = phrase.split()

for search_word in search_words:

	print(search_word)
	stats1, used_photos = photo_parser.main(search_word, 10, used_photos)
	# main_stats = main_stats + stats
	stats2, used_photos = photo_parser.main(search_word, 100, used_photos)
	# main_stats = main_stats + stats
	stats3, used_photos = photo_parser.main(search_word, 1000, used_photos)
	# main_stats = main_stats + stats
	stats4, used_photos = photo_parser.main(search_word, 10000, used_photos)
	# main_stats = main_stats + stats

	single_data_array = stats1 + stats2 + stats3 + stats4

	print(len(single_data_array))
	data_array = data_array + single_data_array
with open('photo_coordinates.json', 'w') as file:
	json.dump(data_array, file)
# drawer.main(stats)