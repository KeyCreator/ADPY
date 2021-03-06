import requests
from mywikipediaapi import get_wiki_urls
from datetime import datetime
import atexit


FILE_URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
FILE_NAME = 'countries.txt'


def named_function_decor(function_name):

    def function_decor(present_function):
        global _file
        _file = open(f'{function_name}.log', 'w', encoding='utf-8')

        def new_function(*args, **kwargs):
            result = present_function(*args, **kwargs)
            _file.write(f'{function_name}({args}, {kwargs}) = {result}\n')

            return result

        return new_function

    return function_decor


@atexit.register
def goodbye():
    _file.close()
    print(f'The file {_file.name} with the function call history is generated')


class Open:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.fp = open(self.file, "w", encoding='utf-8')
        self.fp.write(f'File created {datetime.now()}\n')
        return self.fp

    def __exit__(self, exp_type, exp_value, exp_tr):
        """ suppressing all IOError exceptions """
        if exp_type is IOError:
            self.fp.close()
            return True
        print(f'File {self.file} created')
        self.fp.close()


class Countries:

    def __init__(self, url, session):
        print(f'Get list of countries from {url}')
        resp = session.get(url)
        self.countries_json = resp.json()
        self.countries_count = len(self.countries_json)
        self.start, self.end = -1, self.countries_count
        self.percent, self.progress = 100 / self.countries_count, 0  # for progress bar

    def __iter__(self):
        return self

    @named_function_decor('countries_next')
    def __next__(self):
        self.start += 1
        if self.start == self.end:
            print('')
            raise StopIteration

        self.progress += self.percent
        print('\rProcessing is completed at %3d%%' % self.progress, end='', flush=True)

        return self.countries_json[self.start]['name']['common']


def main():

    with Open(FILE_NAME) as file:
        session = requests.Session()
        for country in Countries(FILE_URL, session):
            file.write(f'{country} - {get_wiki_urls(country, session)[0]}\n')


if __name__ == '__main__':

    main()