from page.page_base import PageBase


class MainPage(PageBase):
    USERNAME_TEXT_XPATH = '//*[@id="root"]/section/main/section/header/div[2]/div/ul/li/div/span'
    LOG_OUT_BUTTON_XPATH = '//*[@id="item_0$Menu"]/li/ul/span[1]'

    PROJECT_LIST_BUTTON_XPATH = '//*[@id="root"]/section/main/section/section/aside/div/ul/li[1]/a/span'
    MY_LIBRARY_BUTTON_XPATH = '//*[@id="root"]/section/main/section/section/aside/div/ul/li[2]/a/span'
    CUBE_LIBRARY_BUTTON_XPATH = '//*[@id="root"]/section/main/section/section/aside/div/ul/li[3]/a/span'

    PROJECT_LIST_TEXT_XPATH = '//*[@id="root"]/section/main/section/section/section/main/div[1]/div[1]/div[1]/span'
    MY_LIBRARY_TEXT_XPATH = '//*[@id="root"]/section/main/section/section/section/main/div[1]/div[1]/div[1]/div[1]/span'
    CUBE_LIBRARY_TEXT_XPATH = '//*[@id="root"]/section/main/section/section/section/main/div[1]/div[1]/div[1]/div[1]/span'

    PROJECT_BUTTON = '//*[@id="contentview"]/div/ul/li[1]/div/div[1]/span'
    # PROJECT_BUTTON = '//*[@id="contentview"]/div/ul/li[2]/div/div[1]/span'

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.url = 'https://dcube.cbim.org.cn/page/project/home/'

    def username_text(self):
        return self.get_element(self.USERNAME_TEXT_XPATH)

    def log_out_button(self):
        return self.get_element(self.LOG_OUT_BUTTON_XPATH)

    def project_list_button(self):
        return self.get_element(self.PROJECT_LIST_BUTTON_XPATH)

    def my_library_button(self):
        return self.get_element(self.MY_LIBRARY_BUTTON_XPATH)

    def cube_library_button(self):
        return self.get_element(self.CUBE_LIBRARY_BUTTON_XPATH)

    def project_list_text(self):
        return self.get_element(self.PROJECT_LIST_TEXT_XPATH)

    def my_library_text(self):
        return self.get_element(self.MY_LIBRARY_TEXT_XPATH)

    def cube_library_text(self):
        return self.get_element(self.CUBE_LIBRARY_TEXT_XPATH)

    def project_button(self):
        return self.get_element(self.PROJECT_BUTTON)