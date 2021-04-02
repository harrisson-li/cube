from business.login import individual_login, corporate_login
import pytest
from business.main_page import verify_username, log_out
from business.init import *
from ddt import ddt, unpack, data


# class TestLogin(TestBase):
class TestLogin:
    # @pytest.mark.usefixtures('setup_teardown_2')
    # @pytest.mark.parametrize("aaa, bbb", [(1, 2), (3, 4)])
    # def test_individual_login_and_logout(self, aaa, bbb):
    @setup_teardown_wrap
    def test_individual_login_and_logout(self):
        # print(setup_teardown)
        # print(aaa)
        # print(bbb)
        username = '李志超'
        individual_login()
        verify_username(username)
        log_out()

    def atest_corporate_login_and_logout(self):
        username = '测试1'
        corporate_login()
        verify_username(username)
        log_out()


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
