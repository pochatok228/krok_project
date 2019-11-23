import photo_parser
import drawer
import json


phrase = input()
used_photos = []
main_stats = []
stats1, used_photos = photo_parser.main(phrase, 10, used_photos)
# main_stats = main_stats + stats
stats2, used_photos = photo_parser.main(phrase, 100, used_photos)
# main_stats = main_stats + stats
stats3, used_photos = photo_parser.main(phrase, 1000, used_photos)
# main_stats = main_stats + stats
stats4, used_photos = photo_parser.main(phrase, 10000, used_photos)
# main_stats = main_stats + stats

data_array = stats1 + stats2 + stats3 + stats4
with open('photo_coordinates.json', 'w') as file:
	json.dump(data_array, file)
# drawer.main(stats)