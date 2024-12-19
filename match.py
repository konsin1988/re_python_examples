import re

s = 'Choose between these two.'
regex = re.compile(r'[A-Za-z]+?\b')


match = re.match(regex, s)
print(f'Первое слово в предложении: {match[0]}')

# ---------------- seed phrase -------------------
s = "neutral choice scout4 rifle tube zone already auto cycle sing ring easily"
regex = re.compile(r'([a-zA-Z]+?\s){11,}[a-zA-Z]+?\b')
match = re.match(regex, s)
print('возможно, это seed-фраза') if match else ''

# --------------- Phone number ----------------------------------
s = '7 942 674 85 53'
regex = re.compile(r'\+{0,1}(\d{1}|\d{3})[\(\s\-]{0,2}\d{3}([\s\-]|(?<=\(\d{3})\)){0,2}\d{3}(?P<sep>[\s\-]{0,2})\d{2}(?P=sep)\d{2}')
match = re.fullmatch(regex, s)
print(True if match else False)

# --------------- Polinomial --------
tests = ['x^3-11x^2+38x-40', '6x^4+19x^3-7x^2-26x+12', '15x^5-8x^4+46x^3+21x^2-21x+3', '4x^6+9x^5-x^4+22x^3-x^2+9x-18', '6x^4+x^3+2x^2-4x+1', 'x', '5x+2', '-x', 'x^2-x', '-9', '-x9', 'x792x', 'xx', '--34', 'x^3+14^x', '-^10']
answers = [True] * 10 + [False] * 6
s = '6x^4+19x^3-7x^2-26x+12'
regex_my = re.compile(r'\-?((\d+|x(\^\d{1,}){0,}|\d+x(\^\d{1,}){0,})[\+\-]){0,}(\d+|x(\^\d{1,}){0,}|\d+x(\^\d{1,}){0,})')
regex = re.compile(r"([+-]?\d*(?:x\^\d+|x)?\b)+")
match = re.fullmatch(regex, s)
print(match[0])

# answers_test = [True if re.fullmatch(regex, x) else False for x in tests]
# print(answers_test)