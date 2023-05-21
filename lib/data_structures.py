spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    new_list = [i["name"] for i in spicy_foods]
    return new_list

def get_spiciest_foods(spicy_foods):
    new_list = [i for i in spicy_foods if i["heat_level"] > 5]
    return new_list

def print_spicy_foods(spicy_foods):
    new_list = [print(f"{i['name']} ({i['cuisine']}) | Heat Level: {'🌶' * i['heat_level'] }") for i in spicy_foods]
    return new_list

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    new_item = [i for i in spicy_foods if cuisine == i["cuisine"]]
    return new_item[0]

def print_spiciest_foods(spicy_foods):
    new_list = [print(f"{i['name']} ({i['cuisine']}) | Heat Level: {'🌶' * i['heat_level'] }") 
                for i in spicy_foods if i["heat_level"] > 5]
    return new_list

def get_average_heat_level(spicy_foods):
    new_list = [i["heat_level"] for i in spicy_foods]
    average = sum(new_list) / len(new_list)
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
