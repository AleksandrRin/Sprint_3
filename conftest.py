import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture
def browser():
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture
def login(browser):
    lk_button = browser.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    lk_button.click()
    email_field = browser.find_element(By.XPATH, '//input[@name="name"]')
    email_field.send_keys('jamespark@example.net')
    password_field = browser.find_element(By.XPATH, '//input[@name="Пароль"]')
    password_field.send_keys('1234567890')
    enter_button = browser.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    enter_button.click()
    yield driver

@pytest.fixture()
def lk_in(login):
    lk_button = login.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    lk_button.click()
    yield driver
