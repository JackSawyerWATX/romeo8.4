fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    split = line.split()
    for word in split:
        if word not in lst:
            lst.append(word)
        else:
            continue

print(sorted(lst))