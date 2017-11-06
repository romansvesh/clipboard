import unittest
from selenium import webdriver

from helpers import helper
from constants import helper_constants


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')

    def test_clipboard_copy_by_button(self):
        self.driver.get("https://clipboardjs.com/")
        helper.click_copy_to_clipboard_button(self.driver)

        self.assertEqual(helper.get_text_from_clipboard(),
                         helper.get_text_from_github_path_field(self.driver))

    def test_clipboard_paste(self):
        self.driver.get("https://ya.ru/")
        helper.set_focus_to_search_input(self.driver)
        helper.send_text_to_clipboard()
        helper.ctrl_v(self.driver)
        self.assertEqual(helper_constants.SOME_TEXT_TO_ENTER,
                         helper.get_text_from_search_input(self.driver))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
