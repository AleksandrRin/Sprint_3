from lokators import Lokator
from faker import Faker

faker = Faker()
email = faker.email()
password = faker.password()


class TestBurgers:

    def test_registration(self, browser): # Тест регистрации
        browser.find_element(*Lokator.ENTER_ACCOUNT).click()
        browser.find_element(*Lokator.REGISTRATION_BUTTON).click()
        browser.find_element(*Lokator.NAME_FIELD).send_keys('Aleksandr')
        browser.find_element(*Lokator.EMAIL_FIELD).send_keys(email)
        browser.find_element(*Lokator.PASSWORD_FIELD).send_keys(password)
        browser.find_element(*Lokator.SIGN_IN_BUTTON).click()

    def test_failed_registration(self, browser): # Тест провальной регистрации
        browser.find_element(*Lokator.ENTER_ACCOUNT).click()
        browser.find_element(*Lokator.REGISTRATION_BUTTON).click()
        browser.find_element(*Lokator.NAME_FIELD).send_keys('Aleksandr')
        browser.find_element(*Lokator.EMAIL_FIELD).send_keys(email)
        browser.find_element(*Lokator.PASSWORD_FIELD).send_keys('12345')
        browser.find_element(*Lokator.SIGN_IN_BUTTON).click()
        wrong_password = browser.find_element(*Lokator.WRONG_PASSWORD_TEXT)
        assert wrong_password.text == 'Некорректный пароль'
