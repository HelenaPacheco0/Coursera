import re

suma = 0
numbers = []

name = input("Enter file:")

file = open(name, 'r')

for line in file:
    line = line.strip()
    numbers = re.findall('[0-9]+', line)
    if numbers != 0 or None:
        for e in range(0, len(numbers)):
            numbers[e] = int(numbers[e])
            suma = suma + numbers[e]
    else:
        continue
    
print(suma)

file.close()
