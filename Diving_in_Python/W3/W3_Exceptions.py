import requests
#import sys

#url = sys.argv[1]
url2 = "https://github.com/"
url = "https://github-not-found.com/"
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print(f"Превышено время ожидания, {url} не отвечает...")
except requests.HTTPError as err:
    print(f"Ошибка доступа, код ошибки: {err.response.status_code}")
except requests.RequestException:
    print(f"Скачивание с {url} не удалось")
else:
    print(response)
