from business.login import corporate_login
from business.init import TestBase
import pytest
from business.main_page import verify_sidebar, verify_click_side_bar, open_project, log_out
from business.project_page import back_to_main_page


class TestMainPage(TestBase):
    def test_side_bar(self):
        corporate_login()
        verify_sidebar()
        log_out()

    def test_click_side_bar(self):
        corporate_login()
        verify_click_side_bar()
        log_out()

    def test_open_and_close_project(self):
        corporate_login()
        open_project()
        back_to_main_page()
        log_out()


if __name__ == '__main__':
    pytest.main([])
