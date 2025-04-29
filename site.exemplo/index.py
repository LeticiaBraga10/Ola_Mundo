 s = 0
c = 0
for c in range(3, 500, 3):
    if c % 3 == 0:
        print('{}'.format(c))
    s +=c
print('A soma de todos os números é:\033[1;32m {} \033[m'.format(s))