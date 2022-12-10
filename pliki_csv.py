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
    total = total +int(content[i][1])
average = total / len(content)

