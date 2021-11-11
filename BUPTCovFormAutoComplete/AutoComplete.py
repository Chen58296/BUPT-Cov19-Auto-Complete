import requests
from requests import HTTPError
import json
import Config


login_url = 'https://app.bupt.edu.cn/uc/wap/login/check'
save_url = 'https://app.bupt.edu.cn/ncov/wap/default/save'
location_url = 'https://api.map.baidu.com/reverse_geocoding/v3/?output=json&coordtype=wgs84ll'






def login():
    data = {
        'username': 'xxxxx',
        'password': 'xxxxx'
    }

    r = requests.post(url=login_url, data=data)

    try:
        r.raise_for_status()
        msg = json.loads(r.text)
        if msg.get("e") == 1:
            return r.cookies
        else:
            raise HTTPError
    except HTTPError:
        print("请求发生错误")


def cov_info_complete(cookies):
    pass


def get_location(url):

    params = {
        'ak':'0hYGiH3Ob5ZhV0eWzrGVXCD3bEdBCi6L',
        'location': '39.968646,116.36244'
    }

    r = requests.get(url=location_url, params=params)

    try:
        r.raise_for_status()
        print(r.url)
        print(r.text)
    except HTTPError:
        print('请求发生错误')


if __name__ == '__main__':
    get_location(location_url)

