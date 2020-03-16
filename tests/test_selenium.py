import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class YandexPassportAuth(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_yandex_passport_auth(self):
        driver = self.driver
        driver.get('https://passport.yandex.ru/auth/add')
        assert "Авторизация" in driver.title
        elem = driver.find_element_by_name("login")
        elem.send_keys("sergey.yu.klimov")
        elem.send_keys(Keys.RETURN)
        assert "Такого аккаунта нет" not in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()