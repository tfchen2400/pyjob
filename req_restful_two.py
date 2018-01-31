import requests,json
if __name__ == '__main__':
    url = "http://www.baidu.com"
    r = requests.get(url)
    print(r.content)
