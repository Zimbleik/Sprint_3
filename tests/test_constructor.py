from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ex_cond
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait


def test_default_select_tab_is_buns(driver):
    # В конструкторе по умолчанию выбрана вкладка булок
    assert "Булки" == driver.find_element(*TestLocators.SELECTED_INGREDIENT_TAB).text

    # Вкладки соусов и начинок не выбраны
    unselected_tabs = driver.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in unselected_tabs:
        assert "Соусы" in tab.text or "Начинки" in tab.text


def test_select_sauces_tab(driver):
    # Клик по вкладке соусов в конструкторе
    sauces = WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.SAUCES_TUB))
    sauces.click()
    WebDriverWait(driver, 10).\
        until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Соусы"))
    assert "Соусы" == driver.find_element(*TestLocators.SELECTED_INGREDIENT_TAB).text

    # Вкладки булок и начинок не выбраны
    unselected_tabs = driver.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in unselected_tabs:
        assert "Булки" in tab.text or "Начинки" in tab.text


def test_select_fillings_tab(driver):
    # Клик по вкладке начинок в конструкторе
    WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.FILLINGS_TUB))
    driver.find_element(*TestLocators.FILLINGS_TUB).click()
    WebDriverWait(driver, 10). \
        until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Начинки"))
    assert "Начинки" == driver.find_element(*TestLocators.SELECTED_INGREDIENT_TAB).text

    # Вкладки булок и соусов не выбраны
    unselected_tabs = driver.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in unselected_tabs:
        assert "Булки" in tab.text or "Соусы" in tab.text


def test_select_buns_tab(driver):
    # Клик по вкладке начинок в конструкторе
    fillings = WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.FILLINGS_TUB))
    try:
        fillings.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click()", fillings)

    # Выбрана вкладка начинки
    WebDriverWait(driver, 10). \
        until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Начинки"))

    # Клик по вкладке булок в конструкторе
    buns = WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.BUNS_TUB))
    try:
        buns.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click()", buns)

    # Выбрана вкладка булок
    WebDriverWait(driver, 10). \
        until(ex_cond.text_to_be_present_in_element(TestLocators.SELECTED_INGREDIENT_TAB, "Булки"))

    # Вкладки соусов и начинок не выбраны
    unselected_tabs = driver.find_elements(*TestLocators.UNSELECTED_INGREDIENT_TABS)
    for tab in unselected_tabs:
        assert "Соусы" in tab.text or "Начинки" in tab.text
