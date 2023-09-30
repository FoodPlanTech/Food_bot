import requests
# import pprint


def get_recipes(id):
    if id:
        payload = {
            'telegram_id': id
            }
        response = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/current-recipe/', params=payload)
        response.raise_for_status()
        return response.json()
    else:
        response = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/teasers')
    response.raise_for_status()
    cards_for_recipe = []
    for recipe in response.json():
        cards_for_recipe.append(recipe)
    print(len(cards_for_recipe))
    return cards_for_recipe


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

# def remember_choice()

def send_subscriber_information():
    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/payments/'   
    payload = {
        "telegram_id": 250714819,
        "preference_ids": [2], 
        "subscription_id": 1
    }
    response_post = requests.post(url, data=payload)
    response_post.raise_for_status()
    return
#def post_preference():
#    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/foodplans/'   
#    payload = {
#    'telegram_id': id
#    'preference_id' : callback_query.data
#        }
#    response_post = requests.post(url, data=payload)
#    response_post.raise_for_status()

