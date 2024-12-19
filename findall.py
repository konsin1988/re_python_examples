import re

s = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'https://imgur.com/hpjus8ds standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scramblhttps://imgur.com/y2lgyvYed it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, rehttps://imgur.com/jJb53h2maining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passhttps://imgur.com/xYy6hjAages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsumhttps://imgur.com/oaUzSly."

regex = re.compile(r'https://imgur.com/[a-zA-Z0-9]{7}')
match = re.findall(regex, s)
print(*match, sep='\n')

# ---------- Поиск почт -------------------
print('-------------Поиск почт----------')
s = 'Dfashu9dasdia spam@example.com shbid@asid nbasdasoidnoasndopjasnodnwaseondfsnhf.dwas@dhnifh.nsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjf buildup@eaglemoss.ru .oasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaif @@@@@.@@ jasp....@@@...dijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid n@w.@a edutrack@ijmo.ru seondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsad ab687848@gmail.com jfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodn vopros@prosv.ru waseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbas spe-elif@mail.ru dasoidnoasndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasd@iashbi@dasid nbasdasoi.@.dnoa@.@sndopjasnodnwaseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmiDfashu9dasdiashbidasid nbasdasoidnoasndopjasnodn mosobleirc@clubonus.ru waseondf isnhfdwasdhnifhnsdaifjaspdijfsadjfoasjdofnasdofnoisdnfoisdanoifnmsiadofmniosdfnmiosnfosnmi'

regex = re.compile(r'((?<=\s)|(?<=^))[a-zA-Z0-9\-_]+?@[a-zA-Z0-9]+?\.[a-zA-Z0-9]+?((?=\s)|(?=\b))')
match = re.finditer(regex, s)

print(*[x[0] for x in match], sep='\n')

# ----------------- Поиск дат ------------------------
print('------------Поиск дат-------------------')
print('''
Найдите все даты в тексте. 
Датой в этом задании будем считать любую последовательность:
nn/nn/nnnn
nnnn/nn/nn
nn.nn.nnnn
nnnn.nn.nn
''')

s = '02.11.2072fs2012,09/18fsdg18/09/2012d2022.20.23d2014,25,03f25\\03\\1864g2015.24.06f2008.24.10'
regex = re.compile(r'(\d{2}(?P<sep>[\.\/])\d{2}(?P=sep)\d{4})|(\d{4}(?P<sep1>[\.\/])\d{2}(?P=sep1)\d{2})')
match = re.finditer(regex, s)
print(*[x[2] for x in match], sep='\n')