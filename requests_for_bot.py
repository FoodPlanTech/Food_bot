import requests
from pay import process_callback_subscribe
from basics import process_start_command, choose_amount
# import pprint

subscription_id = process_callback_subscribe()
telegram_id = process_start_command()
preference_ids = choose_amount()

sub_id = ''.join(c for c in subscription_id if c.isdecimal())
pref_id = ''.join(c for c in preference_ids if c.isdecimal())




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


def send_subscriber_information(telegram_id, pref_id, sub_id):
    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/payments/'   
    payload = {
        "telegram_id": telegram_id,
        "preference_ids": pref_id, 
        "subscription_id": sub_id
    }
    response_post = requests.post(url, data=payload)
    response_post.raise_for_status()
    return


def get_subscribtions():
    response = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/subscriptions/')
    response.raise_for_status()
    subscribtions = response.json()
    return (subscribtions)

#def post_preference():
#    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/foodplans/'   
#    payload = {
#    'telegram_id': id
#    'preference_id' : callback_query.data
#        }
#    response_post = requests.post(url, data=payload)
#    response_post.raise_for_status()

