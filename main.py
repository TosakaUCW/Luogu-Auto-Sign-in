import requests
import json


def punch(Cookie):
    return requests.get(
        'https://www.luogu.com.cn/index/ajax_punch',
        headers={
            "Host": "www.luogu.com.cn",
            "User-Agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language":
            "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://www.luogu.com.cn/",
            "Cache-Control": "no-cache",
            "TE": "Trailers",
            "Cookie": Cookie
        }).text


if __name__ == "__main__":
    f = open("Cookies.txt")
    Cookie = f.readline()
    i = 1
    while Cookie:
        res = punch(Cookie)
        status = json.loads(res)
        print("第 %d 个打卡的结果 : " % i, end="")
        if status['code'] == 200:
            print(status['more']['html'])
        else:
            print(status['message'])
        Cookie = f.readline()
        i += 1
    f.close()