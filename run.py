import photo_parser
from pprint import pprint


def main(phrase=input()):
    main_stats = []
    data_array = []
    used_photos = []
    search_words = phrase.split()

    for search_word in search_words:

        print(search_word)
        single_data_array = photo_parser.main(search_word)

        print(len(single_data_array))
        data_array = data_array + single_data_array
    return data_array


if __name__ == '__main__':
    pprint(len(main()))
