from page.login_page import LoginPage
from business.init import instance
import time
from data.data import corporate_login_data, individual_login_data


def page():
    return LoginPage(instance.driver)


def individual_login(user_name=individual_login_data['user_name'], password=individual_login_data['password']):
    page().open()
    page().normal_user_button().click()
    page().user_name_input().send_keys(user_name)
    page().password_input().send_keys(password)
    time.sleep(3)
    page().login_button().click()


def corporate_login(user_name=corporate_login_data['user_name'], company_code=corporate_login_data['company'],
                    password=individual_login_data['password']):
    page().open()
    page().corporate_user_button().click()
    page().user_name_input().send_keys(user_name)
    page().company_code_input().send_keys(company_code)
    page().password_input().send_keys(password)
    time.sleep(3)
    page().login_button().click()
