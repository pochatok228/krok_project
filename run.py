import photo_parser


def main(phrase=input()):
    main_stats = []
    data_array = []
    used_photos = []
    search_words = phrase.split()

    for search_word in search_words:

        print(search_word)
        stats1, used_photos = photo_parser.main(search_word, 10, used_photos)

        single_data_array = stats1

        print(len(single_data_array))
        data_array = data_array + single_data_array
    return data_array
