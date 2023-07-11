import pytest
from selenium import webdriver
from lokators import Lokator

base_url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture
def browser():
    """
    Фикстура для драйвера
    """
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture
def login(browser):
    """
    Фикстура для авторизации
    """
    browser.find_element(*Lokator.ENTER_ACCOUNT).click()
    browser.find_element(*Lokator.EMAIL_FIELD).send_keys('jamespark@example.net')
    browser.find_element(*Lokator.PASSWORD_FIELD).send_keys('1234567890')
    browser.find_element(*Lokator.ENTER_BUTTON).click()
    yield browser


@pytest.fixture
def lk_in(login):
    """
    Фикстура для входа в личный кабинет
    """
    login.find_element(*Lokator.LK_BUTTON).click()
    yield login
