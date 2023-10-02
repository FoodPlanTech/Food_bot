import requests


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


def send_subscriber_information(telegram_id, pref_id, sub_id, amount):
    url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/payments/'   
    payload = {
        "telegram_id": telegram_id,
        "preference_ids": pref_id, 
        "subscription_id": sub_id,
        "recipes_count": amount

    }
    response_post = requests.post(url, data=payload)
    response_post.raise_for_status()
    return


def get_subscribtions():
    response = requests.get('http://v1131340.hosted-by-vdsina.ru:5555/api/v1/subscriptions/')
    response.raise_for_status()
    subscribtions = response.json()
    return (subscribtions)


def send_rating(value, telegram_id, recipe_id):
    if value == 'like':
        url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/likes/'
    else:
        url = 'http://v1131340.hosted-by-vdsina.ru:5555/api/v1/dislikes/'
    payload = {
        'telegram_id': telegram_id, 
        'recipe_id': recipe_id}
    response_post = requests.post(url, data=payload)
    response_post.raise_for_status()

