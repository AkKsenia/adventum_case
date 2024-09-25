import vk_api
from vk_api.exceptions import VkApiError
from typing import List, Dict
import json
import csv
import datetime as dt


API_VERSION = "5.131"
POSTS_AT_A_TIME = 10000  # предельное число постов

with open("config.json", "r", encoding="utf-8") as config_file:
    f_data = json.load(config_file)

    # access_token для файла config.json можно получить здесь:
    # https://oauth.vk.com/authorize?client_id=5453402&display=page&redirect_uri=http://localhost&scope=&response_type=token&v=5.53

    ACCESS_TOKEN = f_data["access_token"]
    DOMAIN = f_data["domain"]

    AD_ALLOWED = f_data["post_filter"]["ad_allowed"]
    REPOST_ALLOWED = f_data["post_filter"]["repost_allowed"]

    POST_NUMBER = f_data["post_number"]

    del f_data


def get_max_offset(api) -> int:
    try:
        return api.method(
            method="wall.get",
            values={"domain": DOMAIN, "count": POSTS_AT_A_TIME}
        )["count"]
    except VkApiError:
        raise VkApiError("Invalid access token. How to get your own token: "
                         "https://dev.vk.com/api/access-token/getting-started")


def parse_wall_data(api, post_offset) -> List[Dict]:
    data = api.method(method="wall.get", values={
            "domain": DOMAIN,
            "offset": post_offset,
            "count": POSTS_AT_A_TIME
        })["items"]

    return [{
        "time": dt.datetime.fromtimestamp(int(post['date'])).strftime('%Y-%m-%d %H:%M:%S'),
        "likes": post["likes"]["count"],
        "id": post["id"]
    } for post in data]


def main():
    vk_api_ = vk_api.VkApi(token=ACCESS_TOKEN, api_version=API_VERSION)

    max_offset = get_max_offset(vk_api_)
    posts_data = []

    for offset in range(0, max_offset, POSTS_AT_A_TIME):
        posts_data.extend(parse_wall_data(vk_api_, offset))

    with open('posts_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_", "date_", "likes_"])
        for post in posts_data:
            writer.writerow([post["id"], post["time"], post["likes"]])


if __name__ == "__main__":
    main()
