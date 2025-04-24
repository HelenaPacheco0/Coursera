name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

lst = list()
counts = dict()


for line in handle:
    sline = line.strip()

    if sline.startswith('From:'):
        continue
    elif sline.startswith('From'):
        spline = sline.split()

        clock = spline[5]
        time = clock.split(':')

        time2 = time[0].split()

        for x in time2:
            if x not in counts:
                counts[x] = 1
            else:
                counts[x] = counts[x] + 1

for k,v in counts.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)



