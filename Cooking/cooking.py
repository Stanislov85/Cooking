with open('cooking_book.txt', encoding='utf-8') as file:
    print('\nЗадание №1:\n')
    from pprint import pprint
    cook_book = {}
    dish_name_list = []
    for line in file:
        dish_name = line.lower().strip()
        ingredient_count = int(file.readline())
        for i in range(ingredient_count):
            ingredient = file.readline().strip().split('|')
            ingredient_name, quantity, measure = ingredient
            ingridient_dict = dict(ingredient_name = ingredient_name, quantity = int(quantity), measure = measure)
            dish_name_list.append(ingridient_dict)
        cook_book[dish_name] = dish_name_list
        dish_name_list = []
        file.readline()
    pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    print()
    print('\nЗадание №2:\n')
    cook_book_peson = {}
    for dish in dishes:
        if dish in cook_book:
            dish_1 = cook_book[dish]
            for dish_ing in dish_1:
                dish_ing['quantity'] *= person_count
                ingredient_name = dish_ing.pop('ingredient_name')
                if ingredient_name not in cook_book_peson:
                    cook_book_peson[ingredient_name] = dish_ing
                else:
                    cook_book_peson[ingredient_name]['quantity'] +=dish_ing['quantity']
        else:
            print(f'\n{dish} - такого блюда нет!\n')
    pprint(cook_book_peson)
get_shop_list_by_dishes(['запеченный картофель', 'омлет',], 3)
