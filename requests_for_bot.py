import requests
# import pprint


def get_recipes():
    response = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/teasers')
    response.raise_for_status()
    cards_for_recipe = []
    for recipe in response.json():
        cards_for_recipe.append(recipe)
    return cards_for_recipe


def send_id(id):
    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/tg-accounts/'
    payload = {
    'telegram_id': id
        }
    response_post = requests.post(url, data=payload)
    response_post.raise_for_status()


def send_id(id):
    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/tg-accounts/'
    payload = {
    'telegram_id': id
        }
    response_post = requests.post(url, data=payload)
    response_post.raise_for_status()


def get_preferences():
    response = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/preferences')
    response.raise_for_status()
    preferences = response.json()
    return preferences

#def post_preference():
#    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/foodplans/'   
#    payload = {
#    'telegram_id': id
#    'preference_id' : callback_query.data
#        }
#    response_post = requests.post(url, data=payload)
#    response_post.raise_for_status()

