import requests

def search_available_table(restaurant:str, crateria: dict):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


    payload = {
        "page_id": restaurant,
        "locale": "he",
        "criteria": crateria,
        "app": "web", "origin": "page", 
        "sessionId": "4fc186ec-0c85-4e66-a87f-a8e9490b2d2d",
         "stationId": "12682a96-ccfe-43a3-93db-5c1f7bcd7bb0",
          "sendAnalytics": False}

    response = requests.post(
        "https://ontopo.co.il/api/availability/searchAvailability", json=payload, headers=headers)
    return response.json()

