from selenium import webdriver
import pytest


PARAMS = ['default']
IDS = ['default']


class Container:
    driver = None


instance = Container()


class TestBase:
    def setup_class(self):
        instance.driver = webdriver.Chrome()
        instance.driver.maximize_window()

    def teardown_class(self):
        instance.driver.close()
    pass


@pytest.fixture(params=[1, 2, 3, 4], ids=['a', 'b', 'c', 'd'])
def setup_teardown_1(request):
    instance.driver = webdriver.Chrome()
    instance.driver.maximize_window()
    yield
    instance.driver.close()
    print(request.param)


# @pytest.fixture(scope='function', autouse=True, params=PARAMS, ids=IDS)
# def setup_teardown(request):
#     list1 = request.param
#     instance.driver = webdriver.Chrome()
#     instance.driver.maximize_window()
#     yield list1
#     instance.driver.close()


@pytest.fixture(scope='function', params=PARAMS, ids=IDS)
def setup_teardown_2(request):
    list1 = request.param
    instance.driver = webdriver.Chrome()
    instance.driver.maximize_window()
    yield list1
    instance.driver.close()


def setup_teardown_wrap(func):
    def wrap(*args, **kwargs):
        instance.driver = webdriver.Chrome()
        instance.driver.maximize_window()

        func(*args, **kwargs)

        instance.driver.close()

    return wrap
