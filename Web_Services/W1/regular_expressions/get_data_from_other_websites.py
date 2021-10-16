import requests
import re

# # Get Euro to rub relationship
# # result = requests.get('https://www.cbr.ru/currency_base/daily/')
# # html = result.text
#
# # match = re.search(r'Евро\D+(\d+,\d+)', html)
# # rate = match.group(1)
# # print(rate)
#
# html = 'Курс евро на сегодня 89,4388, курс евро на завтра 88,8901'
# # Игнорируем различия регистра(верх-низ)
# match = re.search(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
# rate = match.group(1)
# # print(rate)
#
# # НЕ игнорируем различия регистра(верх-низ)
# match = re.search(r'Евро\D+(\d+,\d+)', html)
# # print(match is None)
#
# # Жадный поиск (*) - оставил минимум справа - 1 цифра, запятая, и цифры
# # print(re.search(r'Евро.*(\d+,\d+)', html, re.IGNORECASE).group(1))
#
# # НЕжадный поиск (*?) - найжем 1й курс
# # print(re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE).group(1))
#
#
# # Используем .findall вместо .research
# # С группами - ()
# match = re.findall(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
# # print(match)
#
# # Без групп
# match = re.findall(r'Евро\D+\d+,\d+', html, re.IGNORECASE)
# # print(match)
#
# # Несколько групп
# match = re.findall(r'Евро\D+(\d+),(\d+)', html, re.IGNORECASE)
# # print(match)
#
# html = """
# Курс евро на сегодня (15 января)
# составляет 89,4388"""
#
# # Добавим флаг re.DOTALL чтобы поззволит точке обозначать переводы строки(\n)
# # print(re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE | re.DOTALL).group(1))
#

# Автомобильные номера
text = '''
Автомобиль с номером A123BC77 подрезал автомоблиь
K654HE197, спровоцировав ДТП с участием еще двух
иномарок с номерами M524OP777 и O007OO77
'''
pattern = r'[ABEKMHOPCTYX]\d{3}[ABEKMHOPCTYX]{2}\d{2,3}'
print(re.findall(pattern, text))
