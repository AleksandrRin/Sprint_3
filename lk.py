from selenium.webdriver.common.by import By
import time

class TestLK:

    def test_open_lk(self, login):
        lk_button = login.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
        lk_button.click()

    def test_open_constructor_from_lk(self, lk_in):
        lk_button = lk_in.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
        lk_button.click()
        constructor_button = lk_in.find_element(By.XPATH, "//p[contains(text(), 'Конструктор')]")
        constructor_button.click()

    def test_click_on_logo_from_lk(self, lk_in):
        logo_button = lk_in.find_element(By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]')
        logo_button.click()

    def test_log_out(self, lk_in):
