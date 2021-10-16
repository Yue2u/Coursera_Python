from bs4 import BeautifulSoup
import unittest
import re
import os
from collections import deque


def parse(path_to_file):
    with open(path_to_file, 'r+', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        article_body = soup.find(id='bodyContent')

        # Count images
        imgs = len(article_body.find_all('img', width=lambda x: int(x or 0) > 199))

        # Count headers
        headers = len([i.text for i in article_body.find_all(name=re.compile(r'h[1-6]')) if i.text[0] in 'ETC'])

        # Count references
        links_len = 0
        for link in article_body.find_all('a'):
            local_link_len = 1
            for i in link.find_next_siblings():
                if i.name == 'a':
                    local_link_len += 1
                else:
                    break
            links_len = max(links_len, local_link_len)

        # Count lists
        lists = 0
        for list_ in article_body.find_all(['ul', 'ol']):
            if not list_.find_parents(['ul', 'ol']):
                lists += 1

    return [imgs, headers, links_len, lists]


def get_next_articles(path, article, a_to_v):
    with open(os.path.join(path, article), 'r', encoding='utf-8') as file:
        links = re.findall(r"(?<=/wiki/)[\w()]+", file.read())

        result = set()
        for link in links:
            if link in a_to_v.keys():
                result.add(a_to_v[link])
        return result


def bfs(path, a_to_v, start_page, pages):
    way = {}

    queue = deque([a_to_v[start_page]])
    visited = set()

    while queue:
        vert = queue.popleft()
        visited.add(vert)

        next_articles_verts = get_next_articles(path, pages[vert], a_to_v)

        for i in next_articles_verts:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                way[i] = vert
    return way


def build_bridge(path, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""
    dir_files = os.listdir(path)
    article_to_vertex = {dir_files[i]: i for i in range(len(dir_files))}

    way = bfs(path, article_to_vertex, start_page, dir_files)

    result = [end_page]
    start = article_to_vertex[start_page]
    v = article_to_vertex[end_page]
    while v != start:
        v = way[v]
        result.append(dir_files[v])
    result.reverse()

    return result

    # напишите вашу реализацию логики по вычисления кратчайшего пути здесь


def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    statistic = {}
    # получаем список страниц, с которых необходимо собрать статистику
    pages = build_bridge(path, start_page, end_page)
    for page in pages:
        statistic[page] = parse(os.path.join(path, page))

    return statistic


STATISTICS = {
    'Artificial_intelligence': [8, 19, 13, 198],
    'Binyamina_train_station_suicide_bombing': [1, 3, 6, 21],
    'Brain': [19, 5, 25, 11],
    'Haifa_bus_16_suicide_bombing': [1, 4, 15, 23],
    'Hidamari_no_Ki': [1, 5, 5, 35],
    'IBM': [13, 3, 21, 33],
    'Iron_Age': [4, 8, 15, 22],
    'London': [53, 16, 31, 125],
    'Mei_Kurokawa': [1, 1, 2, 7],
    'PlayStation_3': [13, 5, 14, 148],
    'Python_(programming_language)': [2, 5, 17, 41],
    'Second_Intifada': [9, 13, 14, 84],
    'Stone_Age': [13, 10, 12, 40],
    'The_New_York_Times': [5, 9, 8, 42],
    'Wild_Arms_(video_game)': [3, 3, 10, 27],
    'Woolwich': [15, 9, 19, 38]}

TESTCASES = (
    ('wiki/', 'Stone_Age', 'Python_(programming_language)',
     ['Stone_Age', 'Brain', 'Artificial_intelligence', 'Python_(programming_language)']),

    ('wiki/', 'The_New_York_Times', 'Stone_Age',
     ['The_New_York_Times', 'London', 'Woolwich', 'Iron_Age', 'Stone_Age']),

    ('wiki/', 'Artificial_intelligence', 'Mei_Kurokawa',
     ['Artificial_intelligence', 'IBM', 'PlayStation_3', 'Wild_Arms_(video_game)',
      'Hidamari_no_Ki', 'Mei_Kurokawa']),

    ('wiki/', 'The_New_York_Times', "Binyamina_train_station_suicide_bombing",
     ['The_New_York_Times', 'Second_Intifada', 'Haifa_bus_16_suicide_bombing',
      'Binyamina_train_station_suicide_bombing']),

    ('wiki/', 'Stone_Age', 'Stone_Age',
     ['Stone_Age', ]),
)


class TestBuildBrige(unittest.TestCase):
    def test_build_bridge(self):
        for path, start_page, end_page, expected in TESTCASES:
            with self.subTest(path=path,
                              start_page=start_page,
                              end_page=end_page,
                              expected=expected):
                result = build_bridge(path, start_page, end_page)
                self.assertEqual(result, expected)


class TestGetStatistics(unittest.TestCase):
    def test_build_bridge(self):
        for path, start_page, end_page, expected in TESTCASES:
            with self.subTest(path=path,
                              start_page=start_page,
                              end_page=end_page,
                              expected=expected):
                result = get_statistics(path, start_page, end_page)
                self.assertEqual(result, {page: STATISTICS[page] for page in expected})


if __name__ == '__main__':
    unittest.main()
