import re
s = 'Recognition is the most powerful motivation factor.'
regex = re.compile(r'\w+?((?=\s)|(?=$)|(?=\b))')

match = re.finditer(regex, s)
print(*[x[0] for x in match], sep='\n')

# --------------- five letters words -----------
s = "Мы вынуждены отталкиваться от того, что разбавленное изрядной долей эмпатии, рациональное мышление способствует подготовке и реализации модели развития. В целом, конечно, консультация с широким активом предоставляет широкие возможности для форм воздействия."
regex = re.compile(r'((?<=\s)|(?<=\b))[a-zA-ZЁ-ё]{5}((?<=\s)|(?<=\b))')
match = re.finditer(regex, s)
s = '\n'.join([x[0] for x in match])

test = """долей
целом"""

print(test == s) 

# ---------------- Парсим ЦБ РФ ----------------------
s = '<div class="main-indicator_rates"><div class="main-indicator_rates-table"><div class="main-indicator_rates-head"><div class="col-md-2 col-xs-7"><a href="/currency_base/">Курсы валют</a></div><div class="col-md-2 col-xs-7 _right"><a href="/currency_base/daily/?UniDbQuery.Posted=True&amp;UniDbQuery.To=20.05.2022">20.05.2022</a></div><div class="col-md-2 col-xs-7 _right"><a href="/currency_base/daily/?UniDbQuery.Posted=True&amp;UniDbQuery.To=21.05.2022">21.05.2022</a></div></div><div class="main-indicator_rate">        <div class="col-md-2 col-xs-9 _dollar">USD</div><div class="col-md-2 col-xs-9 _right mono-num">62,4031 ₽</div><div class="col-md-2 col-xs-9 _right mono-num">58,8862 ₽</div><div class="main-indicator_tooltip" id="V_R01235"><div class="main-indicator_tooltip-head"><button class="main-indicator_tooltip-head-btn _left "></button><div class="main-indicator_tooltip-head-text">17.05.2022 - 21.05.2022</div><button class="main-indicator_tooltip-head-btn _right _disabled "></button></div><table class="main-indicator_tooltip-table"><tr><td class="_day">вт</td><td class="_date">17.05</td><td>63,4445&nbsp;₽</td><td class="_green">-0,3354&nbsp;₽</td></tr><tr><td class="_day">ср</td><td class="_date">18.05</td><td>63,5428&nbsp;₽</td><td class="_red">+0,0983&nbsp;₽</td></tr><tr><td class="_day">чт</td><td class="_date">19.05</td><td>63,5643&nbsp;₽</td><td class="_red">+0,0215&nbsp;₽</td></tr><tr><td class="_day">пт</td><td class="_date">20.05</td><td>62,4031&nbsp;₽</td><td class="_green">-1,1612&nbsp;₽</td></tr><tr><td class="_day">сб</td><td class="_date">21.05</td><td>58,8862&nbsp;₽</td><td class="_green">-3,5169&nbsp;₽</td></tr></table><div class="main-indicator_tooltip-footer">Официальный курс Банка России</div></div></div><div class="main-indicator_rate"><div class="col-md-2 col-xs-9 _euro">EUR</div><div class="col-md-2 col-xs-9 _right mono-num">64,9358 ₽</div><div class="col-md-2 col-xs-9 _right mono-num">60,8953 ₽</div><div class="main-indicator_tooltip" id="V_R01239"><div class="main-indicator_tooltip-head"><button class="main-indicator_tooltip-head-btn _left "></button><div class="main-indicator_tooltip-head-text">17.05.2022 - 21.05.2022</div><button class="main-indicator_tooltip-head-btn _right _disabled "></button></div><table class="main-indicator_tooltip-table"><tr><td class="_day">вт</td><td class="_date">17.05</td><td>65,8166&nbsp;₽</td><td class="_red">+0,0227&nbsp;₽</td></tr><tr><td class="_day">ср</td><td class="_date">18.05</td><td>66,3644&nbsp;₽</td><td class="_red">+0,5478&nbsp;₽</td></tr><tr><td class="_day">чт</td><td class="_date">19.05</td><td>66,6135&nbsp;₽</td><td class="_red">+0,2491&nbsp;₽</td></tr><tr><td class="_day">пт</td><td class="_date">20.05</td><td>64,9358&nbsp;₽</td><td class="_green">-1,6777&nbsp;₽</td></tr><tr><td class="_day">сб</td><td class="_date">21.05</td><td>60,8953&nbsp;₽</td><td class="_green">-4,0405&nbsp;₽</td></tr></table><div class="main-indicator_tooltip-footer">Официальный курс Банка России</div></div></div></div><a class="main-indicator_rates-link" href="/key-indicators/">Все показатели</a></div>'

regex = re.compile(r'\d{1,}?[\.,]\d{0,}\s₽')
match = re.finditer(regex, s)

print(*[x[0] for x in match], sep = '\n')