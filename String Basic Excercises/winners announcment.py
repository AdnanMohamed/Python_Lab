names = ["duck", "gourd", "spitz"]

#using f-strings
for i in range(3):
    names[i]=names[i].capitalize()

for i in names:
    print(f'{i}y Mc{i}face')
print('\n')
#new style
for i in names:
    print("{name}y Mc{name}face".format(name=i))
print('\n')
#using old style

for i in names:
    print("%sy Mc%sface"%(i,i))
