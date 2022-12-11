path = 'C:\\Users\\vdi-student\\Downloads\\rozliczenie.csv'
mode = 'r'
with open(path, mode) as plik:
    content = plik.readlines()

print(content)
for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)


#obliczanie sredniej wyplaty
total = 0
for i in range(1,len(content)):
    total += int(content[i][1])
print('Suma wynagrodzen: ', total)
average = total / (len(content)-1)
print('Srednia wynagrodzen: ', round(average,  2))

#ilosc kobiet na macierzynskim
total = 0
for i in range(1,len(content)):
    print(content[i])
    content[i][4] = content [i][4].replace('\n', '')
    if content[i][3] == 'k' and content[i][4] == 't':
        total += 1
print(total)
