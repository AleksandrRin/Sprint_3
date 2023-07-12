from selenium.webdriver.support.wait import WebDriverWait
from lokators import Lokator
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:
    def test_click_on_filling(self, login):
        """
        Проверка перхода по кнопке НАЧИНКИ
        """
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(Lokator.FILLING_BUTTON)).click()
        assert login.find_element(*Lokator.FILLING_TEXT).is_displayed()

    def test_click_on_bun(self, login):
        """
        Проверка перехода по кнопке БУЛКИ
        """
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(Lokator.FILLING_BUTTON)).click()
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(Lokator.BUN_BUTTON)).click()
        assert login.find_element(*Lokator.BUN_TEXT).is_displayed()

    def test_click_on_sauce(self, login):
        """
        Проверка перехода по кнопке СОУСЫ
        """
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(Lokator.SAUCE_BUTTON)).click()
        assert login.find_element(*Lokator.SAUCE_TEXT).is_displayed()