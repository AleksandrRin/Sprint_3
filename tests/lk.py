import time
from lokators import Lokator
class TestLK:

    def test_open_lk(self, login): # Открытие ЛИЧНОГО КАБИНЕТА
        login.find_element(*Lokator.LK_BUTTON).click()

    def test_open_constructor_from_lk(self, lk_in): # Открытие КОНСТРУКТОРА из личного кабинета
        lk_in.find_element(*Lokator.CONSTRUCTOR_BUTTON).click()

    def test_click_on_logo_from_lk(self, lk_in): # Нажатие на ЛОГО из личного кабинета
        lk_in.find_element(*Lokator.LOGO).click()

    def test_log_out(self, lk_in): # Выход из аккаунта
        time.sleep(2)
        lk_in.find_element(*Lokator.LOG_OUT_BUTTON).click()

