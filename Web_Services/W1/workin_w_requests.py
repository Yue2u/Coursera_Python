import requests
import json

# Make a get request
get_ = requests.get('http://httpbin.org/get')
# print(get_.text)

# Make a post request
post_ = requests.post('http://httpbin.org/post')
# print(post_.text)

# Passing params to get
payload = {'key': 'value1', 'key2': 'value2'}
params_get = requests.get('http://httpbin.org/get', params=payload)
# print(params_get.text)

# Passing params to post/put & e.t.c.
put_ = requests.put('http://httpbin.org/put', data={'key1': 'value1'})
# print(put_.text)

# Passing json params
url = 'http://httpbin.org/post'
json_post_1 = requests.post(url, data=json.dumps({'key1': 'value1'}))
json_post_2 = requests.post(url, json={'key1': 'value1'})
# print(json_post_1.text)
# print(json_post_2.text)

# Passing a Multi-Encoded File
url = 'http://httpbin.org/post'
files = \
    {'file': ('test.txt', open('D:\\Programming\\Workspace\\Python\\Diving_in_python\\Course_3\\W1\\test.txt', 'rb'))}
multi_post = requests.post(url, files=files)
# print(multi_post.text)

# Passing headers
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}
headers_get = requests.get(url, headers=headers)
# print(headers_get.text)

# Response Content
codes_response = requests.get('http://httpbin.org/get')
# print(type(codes_response.text), codes_response.text)  # str
# print(type(codes_response.content), codes_response.content)  # binary
# print(type(codes_response.json()), codes_response.json())  # json

# Response status codes
# print(codes_response.status_code)  # 200
# print(codes_response.status_code == requests.codes.ok)  # True

bad_request = requests.get('http://httpbin.org/status/404')
# print(bad_request.status_code)  # 404
# bad_request.raise_for_status()  # raised HTTPError: 404 Client Error

# Response headers
# print(codes_response.headers)

# Redirection and History
redir_resp = requests.get('http://github.com')
# print(redir_resp.url)
# print(redir_resp.status_code)
# print(redir_resp.history)

# Deny redirection
redir_resp = requests.get('http://github.com', allow_redirects=False)
# print(redir_resp.status_code)
# print(redir_resp.history)

# Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
cookie_req = requests.get(url, cookies=cookies)
# print(cookie_req.text)

# Session objects
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
# print(s.cookies)
# print(r.text)

s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
