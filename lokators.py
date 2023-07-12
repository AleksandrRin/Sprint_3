from selenium.webdriver.common.by import By


class Lokator:
    ENTER_ACCOUNT = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"  # Кнопка ВОЙТИ В АККАУНТ
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"  # Поле ввода EMAIL
    PASSWORD_FIELD = By.NAME, "Пароль"  # Поле ввода PASSWORD
    ENTER_BUTTON = By.XPATH, "//button[contains(text(), 'Войти')]"  # Кнопка ВОЙТИ
    LK_BUTTON = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"  # Кнопка ЛИЧНЫЙ КАБИНЕТ
    RESTORE_BUTTON = By.XPATH, "//a[contains(text(), 'Восстановить пароль')]"  # Кнопка ВОССТАНОВИТЬ ПАРОЛЬ
    ENTER_LINK = By.XPATH, "//a[contains(text(), 'Войти')]"  # Ссылка ВОЙТИ
    REGISTRATION_BUTTON = By.XPATH, '//a[@href="/register"]'  # Ссылка ЗАРЕГИСТРИРОВАТЬСЯ
    NAME_FIELD = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # Поле ввода ИМЯ
    SIGN_IN_BUTTON = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"  # Кнопка ЗАРЕГИСТРИРОВАТЬСЯ
    WRONG_PASSWORD_TEXT = By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"  # Ошибка НЕВЕРНЫЙ ПАРОЛЬ
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]"  # Кнопка КОНСТРУКТОР
    LOGO = By.XPATH, "//div/a[@href='/']"  # Кнопка ЛОГО
    LOG_OUT_BUTTON = By.XPATH, '//button[contains(text(), "Выход")]'  # Кнопка ВЫХОД ИЗ АККАУНТА
    FILLING_BUTTON = By.XPATH, '//span[contains(text(), "Начинки")]'  # Кнопка НАЧИНКИ
    BUN_BUTTON = By.XPATH, '//span[contains(text(), "Булки")]'  # Кнопка БУЛКИ
    SAUCE_BUTTON = By.XPATH, '//span[contains(text(), "Соусы")]'  # Кнопка СОУСЫ
    BUN_TEXT = By.XPATH, "//h2[contains(text(), 'Булки')]"   # Текст Булки
    SAUCE_TEXT = By.XPATH, "//h2[contains(text(), 'Соусы')]"   # Текст СОУСЫ
    FILLING_TEXT = By.XPATH, "//h2[contains(text(), 'Начинки')]"   # Текст НАЧИНКИ