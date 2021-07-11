
l = [[1, 2], [3, 4], [5, 6,7],9]
l.reverse()
for i in l:
    if isinstance(i,list) == True:
        i.reverse()
print(l)