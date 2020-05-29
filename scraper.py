import requests
from bs4 import BeautifulSoup

URL = 'https://www.elespectador.com/noticias/'


def run():
    try:
        response = requests.get(URL)
        # print(response.status_code)
        # print(response.headers)
        # print(response.request.headers)
        # print(response.text)
    except e:
        print('Error', e)




if __name__ == '__main__':
    run()