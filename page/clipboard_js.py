from selenium.webdriver.common.by import By

__COPY_GITHUB_PATH_BUTTON = (By.XPATH, '//button[@data-clipboard-target="#foo"]')
__GITHUB_PATH_FIELD = (By.ID, 'foo')


def get_copy_github_path_button(driver):
    return driver.find_element(*__COPY_GITHUB_PATH_BUTTON)


def get_github_path_field(driver):
    return driver.find_element(*__GITHUB_PATH_FIELD)

