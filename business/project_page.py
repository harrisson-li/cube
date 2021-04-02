from page.project_page import ProjectPage
from business.init import instance
import time
from selenium.webdriver.common.action_chains import ActionChains
from business.main_page import verify_username


def page():
    return ProjectPage(instance.driver)


def back_to_main_page():
    page().back_button().click()
    verify_username('测试1')


def verify_click_side_bar_button():
    hover = ActionChains(page().driver).move_to_element(page().side_bar_button())
    hover.perform()
    time.sleep(2)
    page().wait_for_text(page().SCHEME_DESIGN_BUTTON_XPATH, '方案设计')
    page().scheme_design_button().click()
    time.sleep(2)
    page().xpath_is_visible(page().LINE_BUTTON_XPATH)

    hover.perform()
    page().wait_for_text(page().PARAMETER_DESIGN_BUTTON_XPATH, '参数化设计')
    page().parameter_design_button().click()
    time.sleep(2)
    page().xpath_is_visible(page().CREATE_TAB_XPATH)

    hover.perform()
    page().wait_for_text(page().ME_DESIGN_BUTTON_XPATH, '机电设计')
    page().me_design_button().click()
    time.sleep(2)


def verify_click_parameter_design_tabs():
    hover = ActionChains(page().driver).move_to_element(page().side_bar_button())
    hover.perform()
    time.sleep(2)
    page().parameter_design_button().click()
    time.sleep(2)

    page().assemble_tab().click()
    time.sleep(2)
    page().xpath_is_visible(page().WALL_BUTTON_XPATH)

    page().modify_tab().click()
    time.sleep(2)
    page().xpath_is_visible(page().BOOLEAN_BUTTON_XPATH)

    page().create_tab().click()
    time.sleep(2)
    page().xpath_is_visible(page().LINE_BUTTON_XPATH)


def verify_click_scheme_design_button():
    hover = ActionChains(page().driver).move_to_element(page().side_bar_button())
    hover.perform()
    page().scheme_design_button().click()
    time.sleep(5)

    hover = ActionChains(page().driver).move_to_element(page().line_button())
    hover.perform()
    page().wait_for_text(page().LINE_1_BUTTON_XPATH, '连续直线')
    page().line_1_button().click()
    time.sleep(2)
    hover.perform()
    page().wait_for_text(page().LINE_2_BUTTON_XPATH, '两点线')
    page().line_2_button().click()
    time.sleep(2)

    hover = ActionChains(page().driver).move_to_element(page().rectangle_button())
    hover.perform()
    page().wait_for_text(page().RECTANGLE_1_BUTTON_XPATH, '矩形')
    page().rectangle_1_button().click()
    time.sleep(2)
    hover.perform()
    page().wait_for_text(page().RECTANGLE_2_BUTTON_XPATH, '三点矩形')
    page().rectangle_2_button().click()
    time.sleep(2)
    # hover = ActionChains(page().driver).move_to_element(page().rectangle_button())
    # hover.perform()
    # page().wait_for_text(page().RECTANGLE_3_BUTTON_XPATH, '中心矩形')
    # page().rectangle_3_button().click()
    # time.sleep(2)

    hover = ActionChains(page().driver).move_to_element(page().circle_button())
    hover.perform()
    page().wait_for_text(page().CIRCLE_1_BUTTON_XPATH, '圆心+半径')
    page().circle_1_button().click()
    time.sleep(2)
    hover.perform()
    page().wait_for_text(page().CIRCLE_2_BUTTON_XPATH, '三点圆')
    page().circle_2_button().click()
    time.sleep(2)
    # hover = ActionChains(page().driver).move_to_element(page().circle_button())
    # hover.perform()
    # page().wait_for_text(page().CIRCLE_3_BUTTON_XPATH, '椭圆形')
    # page().circle_3_button().click()
    # time.sleep(2)

    page().polygon_button().click()
    time.sleep(2)

