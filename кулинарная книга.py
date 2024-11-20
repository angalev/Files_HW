# functions
# split string:
def separate_string(string):
    keys = ['ingredient_name', 'quantity', 'measure']
    values = string.split(sep=' | ')
    values[1] = int(values[1])
    return dict(zip(keys, values))

#Create dict with recepies
def file_to_dict(file):
    cook_book = {}
    while True:
        key = file.readline().strip()
        if key == '':
            break
        for i in range(int(file.readline().strip())):
            cook_book.setdefault(key, []).append(
                separate_string(file.readline().strip()))
        file.readline()
    return cook_book

# recepie check
def check(dishes):
    for dish in dishes:
        if dish not in cook_book:
            print(f'{dish} отсутствует в кулинарной книге, исправьте запрос')
    return dish in cook_book

# get shop list
def get_shop_list_by_dishes(dishes, person_count):
    check(dishes)
    dct = {}
    for dish in dishes:
        ingredient_list = cook_book[dish]
        for ingredient in ingredient_list:
            if ingredient['ingredient_name'] not in dct:
                dct.setdefault(ingredient['ingredient_name'],
                    dict(quantity=ingredient['quantity'] * person_count,
                         measure=ingredient['measure']))
            else:
                dct[ingredient['ingredient_name']]['quantity'] = \
                    dct[ingredient['ingredient_name']]['quantity'] + \
                    ingredient['quantity'] * person_count
    return dct

# test wrong request
with open('recipes.txt', encoding='UTF-8') as f:
    dishes = ['Омлет', 'Фахитос', 'Утка по-пекински', 'Изделие из петтиниса']
    cook_book = file_to_dict(f)
    if check(dishes):
        print(cook_book)
        print(get_shop_list_by_dishes(dishes, 2))

# test normal request
with open('recipes.txt', encoding='UTF-8') as f:
    dishes = ['Омлет', 'Фахитос', 'Утка по-пекински']
    cook_book = file_to_dict(f)
    if check(dishes):
        print(cook_book)
        print(get_shop_list_by_dishes(dishes, 2))