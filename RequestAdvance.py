import requests
from requests.auth import HTTPBasicAuth


# # 文件上传
# files = {
#     'file': open('favicon.ico', 'rb')
# }
# r = requests.post("http://httpbin.org/post", files = files)
# print(r.text)

# # Cookies
# r = requests.get('https://www.baidu.com')
# print(r.cookies)

# for key, value in r.cookies.items():
#     print(key + '=' + value)

# # 模拟登陆
# headers = {
#     'Cookies': '_zap=d472331f-0fde-496d-81db-b55869768633; __utma=155987696.1538566226.1521442694.1521442694.1521442694.1; __DAYU_PP=RFBYBVBfifu6fyzrUi3Bffffffffec47064e5ff6; d_c0="AMAkU61Mug2PTm451qE-LIcrTC4O3HkxbK8=|1528620648"; _xsrf=pEU9C77x2rbhsVdfZn7WMCFcspCHpCeK; z_c0="2|1:0|10:1538385138|4:z_c0|92:Mi4xaWQ5WEFnQUFBQUFBd0NSVHJVeTZEU1lBQUFCZ0FsVk44VEtmWEFDVXJpNjF0WklxRUxTQTgwRXNrSTBrUnVlWVZR|77090b848164503d550649ca8a3295ba6df42abd38f598fa7cfec21914636e0a"; tst=r; q_c1=10856453faee4b9a8f34feec605412ca|1541419959000|1514171938000; tgw_l7_route=1b9b7363f02f3a5519d03bdf813bc914',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com', headers = headers)
# print(r.text)

# 会话维持
# 失败！！
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)

# 成功！！！ 
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)


# # SSL 证书验证

# response = requests.get('https://www.12306.cn', verify = False)
# print(response.status_code)


# # 代理设置
# proxies = {
#     'http': '',
#     'https': ''
# }
# requests.get('https://www.taobao.com', proxies = proxies)

# # 超时设置
# r = requests.get('https://www.taobao.com', timeout = 1)
# # r = requests.get('https://www.taobao.com', timeout = (5, 11, 30))
# print(r.status_code)

# # 身份认证
# r.request.get('http://localhost:5000', auth = HTTPBasicAuth('username', 'password'))
# print(r.status_code)

# Prepared Request

url = 'http://httpbin.org/post'
data = {
    'name': 'mike'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

s = requests.Session()
req = requests.Request('POST', url, data = data, headers = headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)