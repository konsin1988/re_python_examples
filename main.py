import re

# regex = re.compile(r'П.+?т')
# s = 'Привет, как тебя Привет зовут?'

# match = re.finditer(regex, s)
# print(
#     type(list(match)[1].re)
# )

regex = re.compile(r'\b[А-Яа-я]+\b')
s2 = 'Второй тест'

match = re.match(regex, s2)

# print(match.group(0))
# print(match.start())
# print(match.end())
# print(match.pos)
# print(match.endpos)
# print(match.re)
# print(match.string)

# -------------II ----------------
regex = re.compile(r'123')
s = '123123'

match = re.match(regex, s)
print(match.group(0) if match != None else '')

