from lokators import Lokator


class TestLogin:
    def test_login_by_enter_account_button(self, browser): # Авторизация через кнопку ВОЙТИ
        browser.find_element(*Lokator.ENTER_ACCOUNT).click()
        browser.find_element(*Lokator.EMAIL_FIELD).send_keys('jamespark@example.net')
        browser.find_element(*Lokator.PASSWORD_FIELD).send_keys('1234567890')
        browser.find_element(*Lokator.ENTER_BUTTON).click()

    def test_login_by_lk_button(self, browser): # Авторизация через кнопку ЛК
        browser.find_element(*Lokator.LK_BUTTON).click()
        browser.find_element(*Lokator.EMAIL_FIELD).send_keys('jamespark@example.net')
        browser.find_element(*Lokator.PASSWORD_FIELD).send_keys('1234567890')
        browser.find_element(*Lokator.ENTER_BUTTON).click()

    def test_login_by_restore_password_form(self, browser): # Авторизация через кнопку ВОССТАНОВИТЬ
        browser.find_element(*Lokator.LK_BUTTON).click()
        browser.find_element(*Lokator.RESTORE_BUTTON).click()
        browser.find_element(*Lokator.ENTER_LINK).click()
        browser.find_element(*Lokator.EMAIL_FIELD).send_keys('jamespark@example.net')
        browser.find_element(*Lokator.PASSWORD_FIELD).send_keys('1234567890')
        browser.find_element(*Lokator.ENTER_BUTTON).click()
