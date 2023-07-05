from selenium.webdriver.common.by import By
import time
class TestLogin:
    def test_login_by_enter_account_button(self, browser):
        enter_account = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
        enter_account.click()
        email_field = browser.find_element(By.XPATH, '//input[@name="name"]')
        email_field.send_keys('jamespark@example.net')
        password_field = browser.find_element(By.XPATH, '//input[@name="Пароль"]')
        password_field.send_keys('1234567890')
        enter_button = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
        enter_button.click()

    def test_login_by_lk_button(self, browser):
        lk_button = browser.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
        lk_button.click()
        email_field = browser.find_element(By.XPATH, '//input[@name="name"]')
        email_field.send_keys('jamespark@example.net')
        password_field = browser.find_element(By.XPATH, '//input[@name="Пароль"]')
        password_field.send_keys('1234567890')
        enter_button = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
        enter_button.click()

    def test_login_by_restore_password_form(self, browser):
        lk_button = browser.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
        lk_button.click()
        restore_button = browser.find_element(By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
        restore_button.click()
        enter_button = browser.find_element(By.XPATH, "//a[contains(text(), 'Войти')]")
        enter_button.click()
        email_field = browser.find_element(By.XPATH, '//input[@name="name"]')
        email_field.send_keys('jamespark@example.net')
        password_field = browser.find_element(By.XPATH, '//input[@name="Пароль"]')
        password_field.send_keys('1234567890')
        enter_button = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
        enter_button.click()

