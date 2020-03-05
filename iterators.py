import requests


WIKI_URL = 'https://en.wikipedia.org/wiki/'
FILE_URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
FILE_NAME = 'countries.txt'


class Countries:

    def __init__(self, url):
        print(f'Get list of countries from {url}')
        resp = requests.get(url)
        self.countries_json = resp.json()
        self.start, self.end = -1, len(self.countries_json)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.countries_json[self.start]['name']['common']


def main():

    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for country in Countries(FILE_URL):
            file.write(f'{country} - {WIKI_URL}{country.replace(" ","_")}\n')
    print(f'File {FILE_NAME} is created')


if __name__ == '__main__':

    main()