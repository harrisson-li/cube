from selenium import webdriver
import pytest


class Container:
    driver = None


instance = Container()


class TestBase:
    def setup_class(self):
        instance.driver = webdriver.Chrome()
        instance.driver.maximize_window()

    def tearDown_class(self):
        instance.driver.close()
