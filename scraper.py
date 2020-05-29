import requests
from bs4 import BeautifulSoup

URL = 'https://www.elespectador.com/noticias/'


def run():

    # --> Use of requests

    try:
        response = requests.get(URL)
    except e:
        print('Error', e)
        
    # Status code
    # print(response.status_code)

    # Headers
    # print(response.headers)

    # Encoding
    # print(response.encoding)

    # Body
    # print(response.text)

    # Request headers
    # print(response.request.headers)

    # Request methods
    # print(response.request.method)

    # --> Use of BeautifulSoup


    # Creating a soup
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(type(soup))

        today = soup.find('div', attrs={
            'class': 'date'
        }).get_text()
        print(today)

        titles_div = soup.find_all('div', attrs={
            'class': 'node-title'
        })
        titles = [titles_div.find('a').get_text() for titles_div in titles_div]
        print(titles)

        with open('result.txt', 'w', encoding='utf-8') as f:
            for title in titles:
                f.write(title)
                f.write('\n')

    else:
        print('Error:', response.status_code)


if __name__ == '__main__':
    run()