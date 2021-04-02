
from page.page_base import PageBase


class LoginPage(PageBase):
    CORPORATE_USER_BUTTON_XPATH = '/html/body/div[2]/ul/li[1]'
    NORMAL_USER_BUTTON_XPATH = '/html/body/div[2]/ul/li[2]'
    USER_NAME_INPUT_XPATH = '//*[@id="userLogin"]/div[1]/input'
    PASSWORD_INPUT_XPATH = '//*[@id="userLogin"]/div[3]/input'
    LOGIN_BUTTON_XPATH = '//*[@id="userLogin"]/div[5]/div'
    COMPANY_CODE_INPUT_XPATH = '//*[@id="userLogin"]/div[2]/input'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.url = 'https://devcas.cbim.org.cn/login?service=https%3A%2F%2Fdcube.cbim.org.cn'

    def corporate_user_button(self):
        return self.get_element(self.CORPORATE_USER_BUTTON_XPATH)

    def normal_user_button(self):
        return self.get_element(self.NORMAL_USER_BUTTON_XPATH)

    def user_name_input(self):
        return self.get_element(self.USER_NAME_INPUT_XPATH)

    def password_input(self):
        return self.get_element(self.PASSWORD_INPUT_XPATH)

    def login_button(self):
        return self.get_element(self.LOGIN_BUTTON_XPATH)

    def company_code_input(self):
        return self.get_element(self.COMPANY_CODE_INPUT_XPATH)
