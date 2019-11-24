import photo_parser
import datetime
from pprint import pprint


def main(phrase, radius=10000, start_time=datetime.datetime(2018, 1, 1)):
    main_stats = []
    data_array = []
    used_photos = []
    search_words = phrase.split(";")
    print(search_words)

    for search_word in search_words:

        print(search_word)
        single_data_array = photo_parser.main(search_word, radius, start_time)

        print(len(single_data_array))
        data_array = data_array + single_data_array
    return data_array


if __name__ == '__main__':
    pprint(main(input()))
