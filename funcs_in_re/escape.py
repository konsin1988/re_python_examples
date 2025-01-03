import re

# -------------- Флешбеки ---------------------
s = r'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !"#$%&\'()*+,-./0123456789:;'
match = re.escape(s)
print(match)

# ------------ Ссылка ------------------------
s = fr'{input()}'
match = re.escape(s)
print(match)