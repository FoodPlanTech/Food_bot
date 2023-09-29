import requests
import collections  
# import pprint

def get_recipes():
    response = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/teasers')
    response.raise_for_status()
    cards_for_recipe = []
    for recipe in response.json():
        cards_for_recipe.append(recipe)
    
    return cards_for_recipe
#     pprint.pprint(cards_for_recipe[0]['image'])

# get_recipes()