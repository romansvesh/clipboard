from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pyperclip

from constants import helper_constants, tech_constants
from page import ya_ru, clipboard_js



def wait_for_element(element, driver, time=tech_constants.TIMEOUT):
    wait = WebDriverWait(driver, time)
    wait.until(expected_conditions.visibility_of(element))


def click_copy_to_clipboard_button(driver):
    wait_for_element(clipboard_js.get_copy_github_path_button(driver), driver)
    clipboard_js.get_copy_github_path_button(driver).click()


def get_text_from_clipboard():
    return pyperclip.paste()


def get_text_from_github_path_field(driver):
    return clipboard_js.get_github_path_field(driver).get_attribute('value')


def send_text_to_clipboard():
    pyperclip.copy(helper_constants.SOME_TEXT_TO_ENTER)


def set_focus_to_search_input(driver):
    wait_for_element(ya_ru.get_search_input(driver), driver)
    driver.execute_script('arguments[0].focus();',
                          ya_ru.get_search_input(driver))


def ctrl_v(driver):
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").perform()


def get_text_from_search_input(driver):
    return ya_ru.get_search_input(driver).get_attribute("value")
