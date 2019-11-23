import json

import vk


def main(search_param):
    with open('districts.json', 'r', encoding='utf-8') as file:
        districts_list = json.load(file)
    # print(districts_list)
    session = vk.Session(access_token='bbb8c82cbbb8c82cbbb8c82c18bbd6ef60bbbb8bbb8c82ce6608e35886c40fa8a7df573')
    vk_api = vk.API(session)
    items = []
    offset = 0
    while True:
        rit = vk_api.photos.search(q=search_param,
                                   lat=55.753960,
                                   long=37.620393,
                                   offset=offset,
                                   radius=2000,
                                   count=1000,
                                   v=5.103)['items']
        if not rit:
            break
        items += rit
        offset += 1000

    array_for_return = []

    for item in items:
        # print(item)
        try:
            item_lat = item['lat']
            item_long = item['long']

            # print(item_lat, item_long )
            if item['sizes']:
                url = item['sizes'][-1]["url"]
            else:
                url = 'None'
            array_for_return.append({"url": url, "lat": item_lat, "long": item_long})

        except Exception as e:
            print(e)

    # теперь парсим инстаграмм

    # print(array_for_return, used_photos)
    return array_for_return
