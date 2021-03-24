f = open("Geert.txt", "r")

list_of_lists = [(line.strip()).split() for line in f]

f.close()

print(list_of_lists)