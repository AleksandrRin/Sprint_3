from lokators import Lokator
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

faker = Faker()
email = faker.email()
password = faker.password()


class TestRegistration:

    def test_registration(self, browser):
        """
        Тест регистрации
        """
        browser.find_element(*Lokator.ENTER_ACCOUNT).click()
        browser.find_element(*Lokator.REGISTRATION_BUTTON).click()
        browser.find_element(*Lokator.NAME_FIELD).send_keys('Aleksandr')
        browser.find_element(*Lokator.EMAIL_FIELD).send_keys(email)
        browser.find_element(*Lokator.PASSWORD_FIELD).send_keys(password)
        browser.find_element(*Lokator.SIGN_IN_BUTTON).click()
        WebDriverWait(browser, 10).until(EC.url_changes(browser.current_url))
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_failed_registration(self, browser):
        """
        Тест провальной регистрации
        """
        browser.find_element(*Lokator.ENTER_ACCOUNT).click()
        browser.find_element(*Lokator.REGISTRATION_BUTTON).click()
        browser.find_element(*Lokator.NAME_FIELD).send_keys('Aleksandr')
        browser.find_element(*Lokator.EMAIL_FIELD).send_keys(email)
        browser.find_element(*Lokator.PASSWORD_FIELD).send_keys('12345')
        browser.find_element(*Lokator.SIGN_IN_BUTTON).click()
        wrong_password = browser.find_element(*Lokator.WRONG_PASSWORD_TEXT)
        assert wrong_password.text == 'Некорректный пароль'