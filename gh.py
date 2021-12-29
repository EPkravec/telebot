s= ['1','2','3','4','5','6','7','21','22','23','222','233','244','2111','222222',]

old_s = ''
gg= 0
for url in s:
    gg += 1
    print(f'{url}')
    if gg == 4:
        old_s = s.index(url)
        print(old_s)
        print(type(old_s))
        print(f'приплыли')
        break

for url in s[old_s:]:
    print(f'{url}')