import requests
import re
from bs4 import BeautifulSoup


# # Get wiki html
# resp = requests.get('https://wikipedia.org/')
# html = resp.text
#
# # Parse html withe RE
# links = re.findall(r'<a[^>]*other-project-link[^>]*href="([^"]*)', html)
# # print(links)
#
# # Parse html withe bs4
# soup = BeautifulSoup(html, 'lxml')
# links = [tag['href'] for tag in soup('a', 'other-project-link')]
# print(links)

# html = """
# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <title>test page</title>
#     </head>
#     <body class="mybody" id="js-body">
#     <p class ="text">first <b>bold</b> paragraph</p>
#     <p class ="text even">second <a href="https://mail.ru">link</a></p>
#     <p class ="text odd">third <a id="paragraph"><b>bold link</b></a></p>
#     </body
# </html>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.b.find_parent('body')['id'], '\n')
# print(soup.p.find_next_sibling(class_="odd"), '\n')
# print(soup.p.find_next_siblings(), '\n')
# print(soup.p.find('b'), '\n')
# print(soup.find(id='js-body')['class'], '\n')
# print(soup.find('b', text='bold'), '\n')
# # print(soup.find_all('p', 'text odd'), '\n')
# # print(soup.find_all(name='p', class_='text odd'), '\n')
# # print(soup.select('p.text.odd'), '\n')
# print(soup.select('p:nth-of-type(3)'), '\n')
# print(soup.select('a > b'))

result = requests.get('https://news.mail.ru/')
html = result.text
soup = BeautifulSoup(html, 'lxml')
print([
    (section.string, [link.string for link in section.find_parents()[4].find_all('span', class_='link__text')])
    for section in soup.find_all('span', class_='hdr__inner')
])

