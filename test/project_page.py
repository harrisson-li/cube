from business.login import corporate_login
from business.init import TestBase
import pytest
from business.main_page import open_project
from business.project_page import verify_click_side_bar_button, verify_click_scheme_design_button, back_to_main_page, \
    verify_click_parameter_design_tabs


class TestProjectPage(TestBase):
    def test_side_bar_button(self):
        corporate_login()
        open_project()
        verify_click_side_bar_button()
        back_to_main_page()

    def test_scheme_design_side_bar(self):
        corporate_login()
        open_project()
        verify_click_scheme_design_button()
        back_to_main_page()

    def test_parameter_design_tabs(self):
        corporate_login()
        open_project()
        verify_click_parameter_design_tabs()
        back_to_main_page()


if __name__ == '__main__':
    pytest.main([])
