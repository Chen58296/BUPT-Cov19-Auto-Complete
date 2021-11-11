import requests
from requests import HTTPError
import json
import Config
import sys


login_url = 'https://app.bupt.edu.cn/uc/wap/login/check'
save_url = 'https://app.bupt.edu.cn/ncov/wap/default/save'


def login(username, password):
    data = {
        'username': username,
        'password': password
    }

    r = requests.post(url=login_url, data=data)

    try:
        r.raise_for_status()
        msg = json.loads(r.text)
        if msg.get("e") == 0:
            return r.cookies
        else:
            raise HTTPError
    except HTTPError:
        print("请求发生错误")


def cov_info_complete(cookies):

    data = {
        'address': Config.ADDRESS,
        'area': Config.AREA,
        'bztcyy': Config.BZTCYY,
        'city': Config.CITY,
        'csmjry': Config.CSMJRY,
        'fjqszgjdq': Config.FJQSZGJDQ,
        'geo_api_info': Config.GEO_API_INFO,
        'glksrq': Config.GLKSRQ,
        'gllx': Config.GLLX,
        'gtjzzchdfh': Config.GTJZZCHDFH,
        'gtjzzfjsj': Config.GTJZZFJSJ,
        'ismoved': Config.ISMOVED,
        'jcbhlx': Config.JCBHLX,
        'jcbhrq': Config.JCBHRQ,
        'jchbryfs': Config.JCHBRYFS,
        'jcjgqr': Config.JCJGQR,
        'jcwhryfs': Config.JCWHRYFS,
        'jhfjhbcc': Config.JHFJHBCC,
        'jhfjjtgj': Config.JHFJJTGJ,
        'jhfjrq': Config.JHFJRQ,
        'mjry': Config.MJRY,
        'province': Config.PROVINCE,
        'qksm': Config.QKSM,
        'remark': Config.REMARK,
        'sfcxtz': Config.SFCXTZ,
        'sfcxzysx': Config.SFCXZYSX,
        'sfcyglq': Config.SFCYGLQ,
        'sfjcbh': Config.SFJCBH,
        'sfjchbry': Config.SFJCHBRY,
        'sfjcwhry': Config.SFJCWHRY,
        'sfjzdezxgym': Config.SFJZDEZXGYM,
        'sfjzxgym': Config.SFJZXGYM,
        'sfsfbh': Config.SFSFBH,
        'sftjhb': Config.SFTJHB,
        'sftjwh': Config.SFTJWH,
        'sfxk': Config.SFXK,
        'sfygtjzzfj': Config.SFYGTJZZFJ,
        'sfyyjc': Config.SFYYJC,
        'sfzx': Config.SFZX,
        'szcs': Config.SZCS,
        'szgj': Config.SZGJ,
        'szsqsfybl': Config.SZSQSFYBL,
        'tw': Config.TW,
        'xjzd': Config.XJZD,
        'xkqq': Config.XKQQ,
        'xwxgymjzqk': Config.XWXGYMJZQK,
        'ymjzxgqk': Config.YMJZXGQK,
        'zgfxdq': Config.ZGFXDQ
    }

    r = requests.post(url=save_url, cookies=cookies, data=data)

    try:
        r.raise_for_status();
        print(r.text)
    except HTTPError:
        print("请求错误")


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    cookies = login(username=username, password=password)
    cov_info_complete(cookies)

