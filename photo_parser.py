import json
import datetime
import vk


def main(search_param, radius=10000, start_time=datetime.datetime(2018, 1, 1)):
    session = vk.Session(access_token='b544a0a6b544a0a6b544a0a612b52a8e99bb544b544a0a6e89e283e80e3120d48417cfc')
    vk_api = vk.API(session)
    items = []
    offset = 0
    while True:
        rit = vk_api.photos.search(q=search_param,
                                   lat=55.620947,
                                   long=37.473815,
                                   offset=offset,
                                   radius=radius,
                                   start_time=start_time,
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
            item_lat = item.get("lat")
            item_long = item.get("long")

            if not item_lat or not item_long:
                continue

            # print(item_lat, item_long )
            if item['sizes']:
                url = item['sizes'][-1]["url"]
            else:
                url = 'None'
            array_for_return.append({"url": url, "lat": item_lat, "long": item_long})

        except Exception as e:
            print("FUCK:", e)

    # print(array_for_return, used_photos)
    return array_for_return
