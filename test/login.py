from business.login import individual_login, corporate_login
from business.init import TestBase
import pytest
from business.main_page import verify_username, log_out


class TestLogin(TestBase):
    def test_individual_login_and_logout(self):
        username = '李志超'
        individual_login()
        verify_username(username)
        log_out()

    def test_corporate_login_and_logout(self):
        username = '测试1'
        corporate_login()
        verify_username(username)
        log_out()


if __name__ == '__main__':
    pytest.main(['-rA'])
