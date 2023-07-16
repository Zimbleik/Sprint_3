from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait


def test_registration_with_correct_data_passes(driver, get_correct_user_data):
    # Переход на форму регистрации
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод корректных данных для регистрации
    driver.find_element(*TestLocators.NAME_FIELD).send_keys(get_correct_user_data.name)
    driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(get_correct_user_data.email)
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(get_correct_user_data.password)

    # Клик по кнопке регистрации
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # Окно сменилось на форму входа
    WebDriverWait(driver, 5).until_not(ex_cond.url_contains("/register"))
    assert "https://stellarburgers.nomoreparties.site/login" == driver.current_url


def test_registration_with_empty_name_failed(driver, get_correct_user_data):
    # Переход на форму регистрации
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод почты и пароля
    email = get_correct_user_data.email
    password = get_correct_user_data.password
    driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке регистрации, когда имя не заполнено
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # Продолжает отображаться форма регистрации с введенной почтой и паролем
    assert driver.find_element(*TestLocators.NAME_FIELD).get_attribute("value") == ""
    assert driver.find_element(*TestLocators.EMAIL_FIELD).get_attribute("value") == email
    assert driver.find_element(*TestLocators.PASSWORD_FIELD).get_attribute("value") == password


def test_registration_with_invalid_email_failed(driver, get_not_correct_user_data):
    # Переход на форму регистрации
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод имени и пароля, формат почты неверен
    name = get_not_correct_user_data.name
    email = get_not_correct_user_data.email
    password = f'{get_not_correct_user_data.password}6'
    driver.find_element(*TestLocators.NAME_FIELD).send_keys(name)
    driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке регистрации
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # Продолжает отображаться форма регистрации с введенными данными
    assert driver.find_element(*TestLocators.NAME_FIELD).get_attribute("value") == name
    assert driver.find_element(*TestLocators.EMAIL_FIELD).get_attribute("value") == email
    assert driver.find_element(*TestLocators.PASSWORD_FIELD).get_attribute("value") == password
    # Отображается ошибка регистрации
    WebDriverWait(driver, 5).until(ex_cond.visibility_of_element_located(TestLocators.ERROR_REGISTRATION))
    assert "Такой пользователь уже существует" == driver.find_element(*TestLocators.ERROR_REGISTRATION).text


def test_registration_when_password_less_6_failed(driver, get_not_correct_user_data):
    # Переход на форму регистрации
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.LINK_REGISTRATION).click()

    # Ввод пароля длинной 5 символов
    driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(get_not_correct_user_data.password)
    # Клик по кнопке регистрации
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON))
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    # Отображается ошибка
    WebDriverWait(driver, 5).until(ex_cond.visibility_of_element_located(TestLocators.ERROR_REGISTRATION))
    assert "Некорректный пароль" == driver.find_element(*TestLocators.ERROR_REGISTRATION).text
