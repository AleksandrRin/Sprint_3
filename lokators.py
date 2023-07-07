from selenium.webdriver.common.by import By


class Lokator:


    ENTER_ACCOUNT = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'  # Кнопка ВОЙТИ В АККАУНТ
    EMAIL_FIELD = By.XPATH, '//input[@name="name"]'  # Поле ввода EMAIL
    PASSWORD_FIELD = By.XPATH, '//input[@name="Пароль"]'  # Поле ввода PASSWORD
    ENTER_BUTTON = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'  # Кнопка ВОЙТИ
    LK_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"  # Кнопка ЛИЧНЫЙ КАБИНЕТ
    RESTORE_BUTTON = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"  # Кнопка ВОССТАНОВИТЬ ПАРОЛЬ
    ENTER_LINK = By.XPATH, "//a[contains(text(), 'Войти')]"  # Ссылка ВОЙТИ
    REGISTRATION_BUTTON = By.XPATH, '//a[@href="/register"]'  # Ссылка ЗАРЕГИСТРИРОВАТЬСЯ
    NAME_FIELD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'  # Поле ввода ИМЯ
    SIGN_IN_BUTTON = By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'  # Кнопка ЗАРЕГИСТРИРОВАТЬСЯ
    WRONG_PASSWORD_TEXT = By.XPATH, '//p[@class="input__error text_type_main-default"]'  # Ошибка НЕВЕРНЫЙ ПАРОЛЬ
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]"  # Кнопка КОНСТРУКТОР
    LOGO = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]'  # Кнопка ЛОГО
    LOG_OUT_BUTTON = By.XPATH, '//button[contains(text(), "Выход")]'  # Кнопка ВЫХОД ИЗ АККАУНТА
    FILLING_BUTTON = By.XPATH, '//span[contains(text(), "Начинки")]' # Кнопка НАЧИНКИ
    BUN_BUTTON = By.XPATH, '//span[contains(text(), "Булки")]' # Кнопка БУЛКИ
    SAUCE_BUTTON = By.XPATH, '//span[contains(text(), "Соусы")]' # Кнопка СОУСЫ
