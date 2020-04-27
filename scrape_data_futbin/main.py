from bs4 import BeautifulSoup
import requests
import json


def extract_data(request):

    print('Starting extracting url...')

    params = {
        'url': request.args.get('url')
    }

    response = requests.get(params['url'])
    soup = BeautifulSoup(response.text, features="html.parser")

    player_id = soup.find_all('div', {'class': 'pversion'})[1].find('a')['data-resource'].replace('p', '')

    url_hourly = 'https://www.futbin.com/20/playerGraph?type=today&year=20&player=' + str(player_id)

    response_hourly = requests.get(url_hourly)
    soup_hourly = BeautifulSoup(response_hourly.text, features="html.parser")

    print('Done')

    return json.dumps(soup_hourly.getText())
