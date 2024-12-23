import re 


# ------------ Гласные запрещены -------------------------
s = 'Especially this one my kinda favourite, and here we go, you dropped it!'

regex = re.compile(r'[aeioyuAEIOUауоыиэяюёеАУОЫИЭЯЮЁЕ]{1}')
match = re.sub(regex, '!', s)
print(match)

# -----------А ты удалил HTML разметку? -----------
s = '<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Timer ⏲</title><link rel="icon" href="./img/goes.png"><link rel="stylesheet" href="./css/normalize.css"><link rel="stylesheet" href="./css/style.css"></head><body><div class="time_wrapper"><h1 class="bold minutes">1:00:00</h1><img class="time" src="./img/start_end.png"></div><div class="buttons"><button class="buttons_button regular start" onclick="start()">Start</button><button class="buttons_button regular notshow pause" onclick="pause()">Pause</button></div></body>'

regex = re.compile(r'<.+?>')
match = re.sub(regex, '', s)
print(match)

# ---------------Бюрократия --------------------------
s1 = 'Ркоман Яна Дмитриевна'

s2 = 'Создатель нелегитимной организации Ркоман Яна Дмитриевна предлагает мне, Трофимову Александру Сергеевичу, подделать документы.'

last_name = s1.split()[0].rstrip('а')
first_name = s1.split()[1][:-1]
second_name = s1.split()[2][:-1]
io = s1.split()[1][0] + '.' + ' ' + s1.split()[2][0] + '.'

regex = re.compile(fr'{last_name}[а-яё]*? ({first_name}[а-яё]*? {second_name}[а-яё]*?((?=\s)|(?=\b))|{io})')
match = re.sub(regex, 'ФИО', s2)
print(match)