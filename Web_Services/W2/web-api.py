import requests
from bs4 import BeautifulSoup
import vk


# Use cbr.ru api
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'xml')
# print(soup.find('CharCode', text='EUR').find_next_sibling('Value').string)  # 89,5427
# print(soup.find(ID='R01239').Value.string)  # 89,5427

# Use OpenWeatherMap.org api
api_key = '2481b27c1a6b46bcb60565c46b5c7efc'
city_name = 'Barnaul'
url = f'https://api.openweathermap.org/data/2.5/weather'
resp = requests.get(url,
                    params={'q': city_name,
                            'appid': api_key,
                            'mode': 'xml',
                            'units': 'metric'})
soup_ = BeautifulSoup(resp.content, 'xml')
# print(soup_.temperature['value'])  # -15

# Use VK api
api_key = 'b997830cb997830cb997830c34b9e1df23bb997b997830cd9b4f3a95596518c6e5bd79a'
url = 'https://api.vk.com/method/users.get'
resp = requests.get(url,
                    params={'access_token': api_key,
                            'user_id': '210700286',
                            'v': '5.89',
                            'fields': 'bdate'})
# print(resp.json()['response'])

# Use vk lib
session = vk.Session()
api = vk.API(session)
# print(api.users.get(user_ids=1, access_token=api_key, v='5.89'))

# session = vk.AuthSession(
#     app_id=7756847,
#     user_login='89021449995',
#     user_password='H5ab!2c!NX83#$S',
# )  # doesnt work cause 2FA
