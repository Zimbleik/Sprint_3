from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait


def test_logout_by_button_in_personal_account(driver):
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
    WebDriverWait(driver, 5).until_not(ex_cond.url_contains("/login"))

    # Переход в личный кабинет
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(ex_cond.url_contains("/account/profile"))

    # Клик по кнопке «Выход» в личном кабинете
    driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until_not(ex_cond.url_contains("/account/profile"))

    # Отображается страница входа
    assert "" == driver.find_element(*TestLocators.EMAIL_FIELD).get_attribute("value")
    assert "" == driver.find_element(*TestLocators.PASSWORD_FIELD).get_attribute("value")
    assert "https://stellarburgers.nomoreparties.site/login" == driver.current_url
