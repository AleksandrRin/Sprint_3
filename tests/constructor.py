import time
from lokators import Lokator


class TestConstructor:
    def test_check_constructor(self, login): # Тест переключения между вкладками конструктора
        time.sleep(1)
        login.find_element(*Lokator.FILLING_BUTTON).click()
        time.sleep(1)
        login.find_element(*Lokator.BUN_BUTTON).click()
        time.sleep(1)
        login.find_element(*Lokator.SAUCE_BUTTON).click()
        time.sleep(1)
