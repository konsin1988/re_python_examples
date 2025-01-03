import re 

# ------------------- .?! --------------------
# Нужно разделить текст на предложения по следующим знакам препинания: .?!.

s = 'Привет, как твои дела? Привет, нормально, учу регулярные выражения.'
regex = re.compile(r'[\.\!\?]')

match = re.split(regex, s)
print(match)

# -------------------- На слова ------------------------
# Разделите текст на слова.
s = 'Привет, как твои дела? Привет, нормально, учу регулярные выражения.'

regex = re.compile(r'[\.,\!\?\s]')
match = re.split(regex, s)
print(match)
# print(*[x for x in match if len(x)>0], sep='\n')

# ----------- База данных магазина ---------------------
# Нужно найти последовательности, подходящие по следующим условиям:

#     Начинается с Категория: 
#     Потом идёт последовательность из кириллических символов обоих регистров и пробелов
#     Минимальная длина последовательности 1 символ
#     Заканчивается на \n

s = 'Категория: Телефоны\nSupreme Burner\nMotorola Razr\nКатегория: Смарт часы и браслеты\nApple Watch 6\nGarmin Venu\nXiaomi Mi Smart Band 6\nКатегория: Игры\nSpore'

regex = re.compile(r'Категория: [Ё-ё\s]+?\n')
match = re.split(regex, s)

print(match)