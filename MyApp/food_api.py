import requests

def get_nutrition_info(food_item):
    api_url = f"https://api.nutritionix.com/v1_1/search/{food_item}"
    headers = {
        "x-app-id": "YOUR_APP_ID",
        "x-app-key": "YOUR_APP_KEY"
    }
    response = requests.get(api_url, headers=headers)
    return response.json()
