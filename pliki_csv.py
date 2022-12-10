path = 'C:\\Users\\vdi-student\\Downloads\\rozliczenie.csv'
mode = 'r'
with open (path, mode) as plik:
    content = plik.readlines()

print(content)
for i in range (len(content)):
    content[i] = content[i].split(',')
print(content)

print(content[3][3])

#obliczanie sredniej wyplaty
total = 0
for i in range (1,len(content)):
    total += int(content[i][1])
average = total / (len(content)-1)
print(round(average,2))

#ilosc kobiet na macierzynskim
for i in range(1,len(content)):
    if content[i][3] == 'k' and content[i][4] == 't' :
        total += 1
print(total)
