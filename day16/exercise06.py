list01 = [4, 5, 566, 7, 8, 10]

list02 = []
for item in list01:
    if item % 2 == 0:
        list02.append(item)

print(list02)


def get_even():
    for item in list01:
        if item % 2 == 0:
            yield item


g01 = get_even()
for item in g01:
    print(item)
