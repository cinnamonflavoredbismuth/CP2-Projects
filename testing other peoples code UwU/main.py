dictionary={1:2,3:4}
for x in dictionary.values():
    for y in dictionary:
        if dictionary[y]==x:
                print(y)