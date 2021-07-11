import re
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l = str(l)
l = l.strip("[]")
end_list = []
number_pattern = '0123456789'
list_word = re.findall(r'[\w]+',l)
list_word = list(list_word)

for i in list_word:
    if i in number_pattern:
        i = int(i)
        end_list.append(i)
    else:
        end_list.append(i)

print(end_list)


