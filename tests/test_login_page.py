from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait


def test_login_by_button_on_main_page(driver):
    # Клик по кнопке «Войти в аккаунт»
    driver.find_element(*TestLocators.ENTER_IN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "Dmitry_simchuk_11_666@gmail.com"
    password = "4321qa"
    driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке входа
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver.current_url


def test_login_by_personal_account_button(driver):
    # Клик по кнопке «Личный кабинет»
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "Dmitry_simchuk_11_666@gmail.com"
    password = "4321qa"
    driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке входа
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver.current_url


def test_login_across_button_in_registration_form(driver):
    # Переход на форму регистрации
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/register"))

    # Клик по ссылке входа
    driver.find_element(*TestLocators.ENTER_LINK).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "Dmitry_simchuk_11_666@gmail.com"
    password = "4321qa"
    driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке входа
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver.current_url


def test_login_across_button_in_password_recovery_form(driver):
    # Переход на форму авторизации
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/login"))

    # Клик по ссылке восстановления пароля
    driver.find_element(*TestLocators.RECOVERY_LINK).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/forgot-password"))

    # Клик по ссылке входа
    driver.find_element(*TestLocators.ENTER_LINK).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/login"))

    # Ввод почты и пароля
    email = "Dmitry_simchuk_11_666@gmail.com"
    password = "4321qa"
    driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке входа
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.ENTER_BUTTON))
    driver.find_element(*TestLocators.ENTER_BUTTON).click()

    # Окно сменилось на главное с кнопкой оформления заказа
    WebDriverWait(driver, 5).until(ex_cond.visibility_of_element_located(TestLocators.ORDER_BUTTON))
    assert "https://stellarburgers.nomoreparties.site/" == driver.current_url
