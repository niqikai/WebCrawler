import requests
import re


# Get请求
r = requests.get('http://httpbin.org/get')
print(r.text)

data = {
    'name': 'mike',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)

# 添加headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
r = requests.get('https://www.zhihu.com/explore', headers = headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 抓取二进制数据
r = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(r.content)



# POST请求
data = {
    'name': 'adam',
    'age': '22'
}
r = requests.post('http://httpbin.org/post', data = data)
print(r.text)





# Get响应
r = requests.get('https://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

# 判断请求是否成功
r = requests.get('https://www.jianshu.com')
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')