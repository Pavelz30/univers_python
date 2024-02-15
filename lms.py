str1 = input()
str2 = input()
str3 = input()

res = ''

if 'зайка' in str1:
    res = str1
if 'зайка' in str2:
    if res == '' or res > str2:
        res = str2
if 'зайка' in str3:
    if res == '' or res > str3:
        res = str3

print(res, len(res))