import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6140613415:AAEKrpsnY4Kjg6tPXlcH-adKG5GBGrZrpoM'
TEXT: str = 'Cograts! u get new update !!! :3'
MAX_COUNTER: int = 100
API_FOXES_URL: str = 'https://randomfox.ca/floof/'
ERROR_TEXT: str = 'All foxes are busy right now :c Try again, please'

offset: int = -2
counter: int = 0
fox_response: requests.Response
fox_link: str

while counter < MAX_COUNTER:
    print('attempt = ', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    print(updates)
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            fox_response = requests.get(API_FOXES_URL)
            if fox_response.status_code == 200:
                fox_link = fox_response.json()['image']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?caht_id={chat_id}&text={TEXT}')
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}\
                    &photo={fox_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?caht_id={chat_id}\
                             &text={ERROR_TEXT}')

time.sleep(1)
counter += 1
