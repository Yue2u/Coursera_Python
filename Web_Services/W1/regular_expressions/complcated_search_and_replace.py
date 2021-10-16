import re
nicknames = ['sU3r_h4XX0r', 'alёna', 'ivan ivanovich']
reg = re.compile(r'^\w+$', re.ASCII)
for nick in nicknames:
    pass
    # print('{} nickname: "{}"'.format('valid' if reg.match(nick) else 'invalid', nick))

text = ('Анна и Лена загорали на берегу океана, '
        'когда к ним подошли Яна, ПОЛИНА и Ильнар')

# print(re.findall(r'[А-Я]\w*на', text))

# print(re.findall(r'\b[А-Я]\w*(?:на|НА)\b', text))

text = "Как защитить металл от процесса коррозии?"

print(re.findall(r'(\w)\1', text))

print(re.sub(r'а', '?', text))

print(re.sub(r'(\w)\1', lambda r: r.group(0).upper(), text))

print(re.sub(r'\b(\w*(\w)\2\w*)\b', r'[\1]', text))
