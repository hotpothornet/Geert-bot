f = open("Geert.txt", "r")
lines = []

for line in f.readlines():
    lines.append(line.replace('\n', ''))

print(lines)

f.close()
