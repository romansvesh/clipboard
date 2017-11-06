from selenium.webdriver.common.by import By

__SEARCH_INPUT = (By.ID, 'text')


def get_search_input(driver):
    return driver.find_element(*__SEARCH_INPUT)
