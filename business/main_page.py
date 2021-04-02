from page.main_page import MainPage
from business.init import instance
from page.project_page import ProjectPage
import time
from selenium.webdriver.common.action_chains import ActionChains
from page.login_page import LoginPage


def page():
    return MainPage(instance.driver)


def log_out():
    hover = ActionChains(page().driver).move_to_element(page().username_text())
    hover.perform()
    time.sleep(2)
    # page().wait_for_text(page().LOG_OUT_BUTTON_XPATH, '退出登录')
    page().log_out_button().click()
    LoginPage(instance.driver).wait_for_text(LoginPage(instance.driver).LOGIN_BUTTON_XPATH, '登录')
    time.sleep(2)


def verify_username(user_name):
    assert page().username_text().text == user_name
    time.sleep(5)


def verify_sidebar():
    assert page().xpath_is_visible(page().PROJECT_LIST_BUTTON_XPATH)
    assert page().xpath_is_visible(page().MY_LIBRARY_BUTTON_XPATH)
    assert page().xpath_is_visible(page().CUBE_LIBRARY_BUTTON_XPATH)


def verify_click_side_bar():
    page().my_library_button().click()
    time.sleep(3)
    page().wait_for_text(page().MY_LIBRARY_TEXT_XPATH, '我的构件库')

    page().cube_library_button().click()
    time.sleep(3)
    page().wait_for_text(page().CUBE_LIBRARY_TEXT_XPATH, 'CUBE构件库')

    page().project_list_button().click()
    time.sleep(3)
    page().wait_for_text(page().PROJECT_LIST_TEXT_XPATH, '项目列表')


def open_project():
    page().project_button().click()
    ProjectPage(instance.driver).xpath_is_visible(ProjectPage(instance.driver).SIDE_BAR_BUTTON_XPATH)
    ProjectPage(instance.driver).loading_text_disappear()
    time.sleep(5)
