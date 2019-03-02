# def get_omelet_ingredients(omelet_name):
#     ingredients = {'eggs': 2, 'milk': 1}
#     if omelet_name == 'cheese':
#         ingredients['cheese'] = 2
#     elif omelet_name == 'western':
#         ingredients['jack_cheese'] = 2
#         ingredients['ham'] = 1
#         ingredients['pepper'] = 1
#         ingredients['onion'] = 1
#     elif omelet_name == 'greek':
#         ingredients['feta_cheese'] = 2
#         ingredients['spinach'] = 2
#     else:
#         print('that is not on the menu, sorry!')
#         return None
#     return ingredients


def make_food(ingredients_needed, food_name):
    for ingredient in ingredients_needed.keys():
        print('adding %d of %s to make a %s' %
              (ingredients_needed[ingredient], ingredient, food_name))
    print('made %s ' % food_name)
    return food_name


def in_fridge(some_fridge, desired_item):
    try:
        count = some_fridge[desired_item]
    except KeyError:
        count = 0
    return count


def make_omelet(omelet_type):
    def get_omelet_ingredients(omelet_name):
        ingredients = {'eggs': 2, 'milk': 1}
        if omelet_name == 'cheese':
            ingredients['cheese'] = 2
        elif omelet_name == 'western':
            ingredients['jack_cheese'] = 2
            ingredients['ham'] = 1
            ingredients['pepper'] = 1
            ingredients['onion'] = 1
        elif omelet_name == 'greek':
            ingredients['feta_cheese'] = 2
            ingredients['spinach'] = 2
        else:
            print('that is not on the menu, sorry!')
            return None
        return ingredients
    if type({}) == type(omelet_type):
        print('omelet_type is a dictionary with ingredients')
        return make_food(omelet_type, 'omelet')
    elif type(omelet_type) == type(''):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        return make_food(omelet_ingredients, omelet_type)
    else:
        print("i don't think i can make this kind of omelet: %s" % omelet_type)


omelet_type = make_omelet('cheese')
print(omelet_type)
omelet_type = make_omelet({'eggs': 2, 'jack_cheese': 2, 'milk': 1, 'mushrooms': 2})
print(omelet_type)
