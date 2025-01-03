import re
regex = re.compile(r'[Кк]од')
s = '''Хочу полететь на Марс(
Секретный код: Dogecoin
Батут работает!
Где ключи от моей Tesla?'''
result = re.search(regex, s)

# if result != None:
#     new_lines = list(re.finditer('\n', s[:result.start()]))
#     new_lines_count = 1 if new_lines is None else new_lines.__len__() + 1
#     start_in_line = re.search(regex, s[:result.end()]).start() if new_lines_count == 1 else re.search(regex, s[new_lines[-1].start()+1:result.end()]).start()
#     print(new_lines_count, start_in_line)
# else:
#     print('код не найден')



# ------------------------ II -----------------
s = '''Activation key: ZxHMR-TVFQE-QUEP7-ZRYOV-7SPEX
JFP9D-7C4Z9-XHFMD-KH3TX-NTS6Z
Activatin key: ONHVS-A705Q-QIWMB-3TRKD-93JQV
gg key: J4DP3-WT02L-VK1DN-36ET7-MEKYI
Activation key: 9KAOG-UTB4I-6JAE3-75BR2-IB27P'''
s = s.split('\n')

regex = re.compile(r'(?<=Activation key: )([\dA-Z]{5}-){4}[\dA-Z]{5}')

# for i in s:
#     match = re.search(regex, i)
#     if match != None:
#         print(match[0])
#         break


# ------------------- III ---------------------------------
s = r'{"errorCode":909,"errorMessage":"Are you a robot? Please enter the captcha below","errorDescription":null,"logStatus":null,"captcha":"\/captcha\/view?_CAPTCHA&amp;t=0.4234253455+1543553431"}'

regex = re.compile(r't=[\d\.\+]+?(?=")')

match = re.search(regex, s)
print(match)