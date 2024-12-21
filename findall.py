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
print(*[x[0] for x in match], sep='\n')

# ------------------ Какое сейчас время? ------------------
print('---------------Какое сейчас время?----------------')
print('''
Нужно найти последовательности, подходящие по следующим условиям:

    Часы от 0 до 23
    Потом идёт :
    Минуты от 0 до 59
    Если в последовательности количество часов или минут меньше 10, то перед ним стоит 0
    Не является подпоследовательностью
''')

s = '05:51 22:57 23:02 07:64 14:73 09:09 09:51 47:61 48:17 52:74 77:29 12:25 06:39 36:26 02:06 09:37 69:11 58:50 20:70 25:44 18:66 41:52 39:41 48:77 65:62 23:32 60:07 73:13 71:79 67:64 15:28 46:74 22:03 42:10 18:56 49:24 78:66 07:48 04:47 49:78 18:42 45:16 01:64 26:39 06:01 72:58 76:75 75:13 44:58 53:50 46:25 00:47 00:18 78:69 36:60 28:08 13:00 42:73 37:54 29:66 14:26 21:66 16:46 49:03 52:33 34:40 75:73 57:35 36:22 24:63 38:77 58:77 76:17 65:73 46:03 47:42 26:35 76:41 32:73 62:76 77:12 56:44 48:27 37:25 73:77 79:79 76:29 44:05 66:47 20:11 38:00 02:22 33:50 53:16 29:17 47:62 21:16 33:02 76:37 11:43'

regex = re.compile(r'([0-1][0-9]|[2][0-3]):[0-5][0-9]')
match = re.finditer(regex, s)
print(*[x[0] for x in match], sep='\n')
# print(len([x for x in match]))

test = print(len(str.split('''05:51
22:57
23:02
09:09
09:51
12:25
06:39
02:06
09:37
23:32
15:28
22:03
18:56
07:48
04:47
18:42
06:01
00:47
00:18
13:00
14:26
16:46
20:11
02:22
21:16
11:43''', '\n')))

print('-----------------Все ссылки a--------------')
print('''
Выведите все ссылки, которые находятся в тегах a:

<a target="_blank" href="https://stepik.org/">Hyperlink</a>
Должно вывести:
        https://stepik.org/''')

s = '<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Пролистай вниз</title><link rel="stylesheet" href="./css/normalize.css"><link rel="stylesheet" href="./css/style.css"><link rel="icon" href="./img/icon.jpg"></head><body><header><h1 class="privet">Привет!<br>Пролистай страничку вниз.</h1><img src="./img/photo.jpg" alt="" class="logo_icon"></header><main><p class="paragraph">Чтобы продолжить - отправь боту любое фото.</p></main><footer><a class="link" href="./img/photo.jpg" download="">Фото</a><p class="link">id стикера - CAACAgIAAxkBAAIDxWITCaZnaUelQ0SNlHMTrjd2klAmAAIBAQACVp29CiK-nw64wuY0IwQ</p><a class="link" href="./img/tochno.txt" download="">Документ</a></footer></body></html>'

regex_a = re.compile(r'<a.+?>')
regex_href = re.compile(r'(?<=href=").+?(?=")')
match_a = re.finditer(regex_a, s)
# for x in match_a:
#     print(re.search(regex_href, x)[0])
print(*[re.search(regex_href, x[0])[0] for x in match_a], sep='\n')