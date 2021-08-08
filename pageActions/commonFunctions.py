from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Automation:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)

    def open_browser(self, url):
        self.browser.get(url)
        time.sleep(5)

    def get_page_title(self):
        return self.browser.title

    def get_element_text(self, xpath):
        return self.browser.find_element(By.xpath).text()

    def clear_element_input_text(self, xpath):
        self.browser.find_element(By.xpath).clear()


    def click_on_element(self, x_path):
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).click()

    def click_on_inputs_send_keys(self, x_path, value):
        time.sleep(3)
        self.browser.find_element(By.XPATH, x_path).send_keys(value)

    def selelct_value_from_drop_down(self, xpath, value):
        time.sleep(3)
        select = Select(self.browser.find_element(By.XPATH, xpath))
        select.select_by_value(value)

    def minimize_browser(self):
        self.browser.maximize_window()

    def maximize_browser(self):
        self.browser.maximize_window()

    def alert_handler(self):
        alert_obj = self.browser.switch_to.alert()
        print(f"Alert : {alert_obj.text}")
        alert_obj.dismiss()


# facebook = Automation()
# facebook.open_browser("https://www.facebook.com/")
# title = facebook.get_page_title()
# print(title)
# facebook.click_on_inputs_send_keys('//input[@name="email"]', '-----')
# facebook.click_on_inputs_send_keys('//input[@name="pass"]', '-------')
# facebook.click_on_element('//button[@name="login"]')
# time.sleep(10)
# facebook.alert_handler()
