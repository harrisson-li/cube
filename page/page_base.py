from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class PageBase:
    def __init__(self, driver):
        self.driver = driver
        self.url = ''

    def open(self):
        self.driver.get(self.url)

    def get_element(self, xpath, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def xpath_is_visible(self, xpath, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

    def wait_for_text(self, xpath, text, timeout=30):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), text))

    def element_is_invisible(self, element, timeout=120):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element(element))
