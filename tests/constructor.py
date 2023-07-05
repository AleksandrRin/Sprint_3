import time

from selenium.webdriver.common.by import By


class TestConstructor:
    def test_check_constructor(self, login):
        time.sleep(2)
        bun_button = login.find_element(By.XPATH, '//span[contains(text(), "Булки")]')
        bun_button.click()
        sauce_button = login.find_element(By.XPATH, '//span[contains(text(), "Соусы")]')
        sauce_button.click()
        filling_button = login.find_element(By.XPATH, '//span[contains(text(), "Начинки")]')
        filling_button.click()