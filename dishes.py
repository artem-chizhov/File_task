def to_read(name_file):
    cook_book = {}

    with open(name_file,'r', encoding='utf-8') as f:
    
        for i in f:
            if i != "\n":
                ingredients_list = []
                num = int(f.readline())
                for test in range(num):
                    ingredient_dict = {}
                    item1, item2, item3 = f.readline().split("|")
                    ingredient_dict['ingredient_name'] = item1.strip(' ')
                    ingredient_dict['quantity'] = item2.strip(' ')
                    ingredient_dict['measure'] = item3.strip(' \n')
                    ingredients_list.append(ingredient_dict)
                    cook_book[i.strip()] = ingredients_list
            else:
                continue
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    output_= {}
    for dish in dishes:
        for counter in range(len(to_read('recipes.txt')[dish])):
            ingredient_name = to_read('recipes.txt')[dish][counter]["ingredient_name"]
            quantity = to_read('recipes.txt')[dish][counter]["quantity"]
            measure = to_read('recipes.txt')[dish][counter]["measure"]
            if ingredient_name not in output_.keys():
                output_[ingredient_name] = {'measure' : measure, 'quantity' : str(int(quantity)*person_count)}
            else:
                output_[ingredient_name].update({'measure' : measure, 'quantity' : int(output_[ingredient_name]["quantity"]) + int(quantity)*person_count})
    return output_



print("===================="*5)
for key, value in get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10).items():
  print("{0}: {1}".format(key,value))

print("===================="*5)
for key, value in to_read('recipes.txt').items():
  print("{0}: \n{1}\n".format(key,value))
print("===================="*5)