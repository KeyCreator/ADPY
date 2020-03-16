import unittest
import requests

API_KEY = 'trnsl.1.1.20200126T054625Z.88e7966dda452db5.eb5f3f3cbd027071eeab928892e4003aee58a923'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate(text, from_lang='en', to_lang='ru'):

    params = {
        'key': API_KEY,
        'lang': f'{from_lang}-{to_lang}',
    }
    data = {
        'text': text
    }
    resp = requests.post(URL, params=params, data=data)
    resp_json = resp.json()
    translate_text = ''

    if resp_json['code'] == 200:
        translate_text = resp_json['text'][0]

    return resp_json['code'], translate_text

class TestTranslate(unittest.TestCase):

    def test_translate_hello(self):
        resp_code, text = translate('Hello')
        self.assertEqual(resp_code, 200)
        self.assertEqual(text.lower(), 'привет')

    def test_wrong_to_lang(self):
        resp_code, text = translate('Hello', to_lang='00')
        self.assertNotEqual(resp_code, 200)

    def test_wrong_translate_hello(self):
        resp_code, text = translate('Hello')
        self.assertEqual(resp_code, 200)
        self.assertNotEqual(text.lower(), 'до свидания')


if __name__ == '__main__':
    unittest.main()
