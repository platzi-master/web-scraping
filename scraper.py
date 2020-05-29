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

    except e:
        print('Error', e)


if __name__ == '__main__':
    run()