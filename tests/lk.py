import time

from lokators import Lokator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLK:

    def test_open_lk(self, login):
        """
        Открытие ЛИЧНОГО КАБИНЕТА
        """
        login.find_element(*Lokator.LK_BUTTON).click()
        WebDriverWait(login, 10).until(EC.url_changes(login.current_url))
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_open_constructor_from_lk(self, login):
        """
        Открытие КОНСТРУКТОРА из личного кабинета
        """
        login.find_element(*Lokator.LK_BUTTON).click()
        login.find_element(*Lokator.CONSTRUCTOR_BUTTON).click()
        assert login.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_click_on_logo_from_lk(self, lk_in):
        """
        Нажатие на ЛОГО из личного кабинета
        """
        lk_in.find_element(*Lokator.LOGO).click()
        assert lk_in.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_log_out(self, lk_in):
        """
        Выход из аккаунта
        """
        WebDriverWait(lk_in, 10).until(EC.element_to_be_clickable(Lokator.LOG_OUT_BUTTON)).click()
        WebDriverWait(lk_in, 10).until(EC.url_changes(lk_in.current_url))
        assert lk_in.current_url == 'https://stellarburgers.nomoreparties.site/login'