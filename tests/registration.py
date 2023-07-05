from selenium.webdriver.common.by import By
import time
from faker import Faker

faker = Faker()
email = faker.email()
class TestBurgers:

    def test_registration(self, browser):
        enter_account = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
        enter_account.click()
        registration_button = browser.find_element(By.XPATH, '//a[@href="/register"]')
        registration_button.click()
        name_field = browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_field.send_keys('Aleksandr')
        email_field = browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        email_field.send_keys(email)
        password_field = browser.find_element(By.XPATH, '//input[@name="Пароль"]')
        password_field.send_keys('1234567890')
        sign_in_button = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
        sign_in_button.click()
        print(email)
    def test_failed_registration(self, browser):
        enter_account = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
        enter_account.click()
        registration_button = browser.find_element(By.XPATH, '//a[@href="/register"]')
        registration_button.click()
        name_field = browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_field.send_keys('Aleksandr')
        email_field = browser.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        email_field.send_keys(email)
        password_field = browser.find_element(By.XPATH, '//input[@name="Пароль"]')
        password_field.send_keys('12345')
        sign_in_button = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
        sign_in_button.click()
        wrong_password_text = browser.find_element(By.XPATH, '//p[@class="input__error text_type_main-default"]')
        assert wrong_password_text.text == 'Некорректный пароль'
        print(email)


