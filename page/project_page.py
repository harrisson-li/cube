from page.page_base import PageBase


class ProjectPage(PageBase):
    SIDE_BAR_BUTTON_XPATH = '//*[@id="root"]/section/header/div[1]/div[3]/div/ul/li[2]/div/div/div[2]'
    LOADING_TEXT_XPATH = '//*[@id="mask-tip"]'
    BACK_BUTTON_XPATH = '//*[@id="root"]/section/header/div[1]/div[1]/span[1]'

    SCHEME_DESIGN_BUTTON_XPATH = '//*[@id="item_0$Menu"]/li[1]/span'
    PARAMETER_DESIGN_BUTTON_XPATH = '//*[@id="item_0$Menu"]/li[2]/span'
    ME_DESIGN_BUTTON_XPATH = '//*[@id="item_0$Menu"]/li[3]/span'

    CREATE_TAB_XPATH = '//*[@id="rc-tabs-3-tab-0"]/div'
    ASSEMBLE_TAB_XPATH = '//*[@id="rc-tabs-3-tab-1"]/div'
    MODIFY_TAB_XPATH = '//*[@id="rc-tabs-3-tab-2"]/div'

    LINE_BUTTON_XPATH = '//*[@id="rc-tabs-3-panel-0"]/div[2]/div[2]/ul/li[1]'
    LINE_1_BUTTON_XPATH = '//*[@id="104111$Menu"]/li[1]/span'
    LINE_2_BUTTON_XPATH = '//*[@id="104111$Menu"]/li[2]/span'

    RECTANGLE_BUTTON_XPATH = '//*[@id="rc-tabs-3-panel-0"]/div[2]/div[2]/ul/li[2]'
    RECTANGLE_1_BUTTON_XPATH = '//*[@id="104121$Menu"]/li[1]/span'
    RECTANGLE_2_BUTTON_XPATH = '//*[@id="104121$Menu"]/li[2]/span'
    RECTANGLE_3_BUTTON_XPATH = '//*[@id="104121$Menu"]/li[3]/span'

    POLYGON_BUTTON_XPATH = '//*[@id="rc-tabs-3-panel-0"]/div[2]/div[2]/ul/div/div/div/div'

    CIRCLE_BUTTON_XPATH = '//*[@id="rc-tabs-3-panel-0"]/div[2]/div[2]/ul/li[3]'
    CIRCLE_1_BUTTON_XPATH = '//*[@id="104141$Menu"]/li[1]/span'
    CIRCLE_2_BUTTON_XPATH = '//*[@id="104141$Menu"]/li[2]/span'
    CIRCLE_3_BUTTON_XPATH = '//*[@id="104141$Menu"]/li[3]/span'

    WALL_BUTTON_XPATH = '//*[@id="rc-tabs-3-panel-1"]/div[2]/div[2]/ul/div[1]'

    BOOLEAN_BUTTON_XPATH = '//*[@id="rc-tabs-3-panel-2"]/div[2]/div[2]/ul/li'

    def __init__(self, driver):
        super(ProjectPage, self).__init__(driver)

    def back_button(self):
        return self.get_element(self.BACK_BUTTON_XPATH)

    def side_bar_button(self):
        return self.get_element(self.SIDE_BAR_BUTTON_XPATH, timeout=120)

    def loading_text(self):
        return self.get_element(self.LOADING_TEXT_XPATH)

    def loading_text_disappear(self):
        return self.element_is_invisible(self.loading_text())

    def scheme_design_button(self):
        return self.get_element(self.SCHEME_DESIGN_BUTTON_XPATH)

    def parameter_design_button(self):
        return self.get_element(self.PARAMETER_DESIGN_BUTTON_XPATH)

    def me_design_button(self):
        return self.get_element(self.ME_DESIGN_BUTTON_XPATH)

    def create_tab(self):
        return self.get_element(self.CREATE_TAB_XPATH)

    def assemble_tab(self):
        return self.get_element(self.ASSEMBLE_TAB_XPATH)

    def modify_tab(self):
        return self.get_element(self.MODIFY_TAB_XPATH)

    def line_button(self):
        return self.get_element(self.LINE_BUTTON_XPATH)

    def line_1_button(self):
        return self.get_element(self.LINE_1_BUTTON_XPATH)

    def line_2_button(self):
        return self.get_element(self.LINE_2_BUTTON_XPATH)

    def rectangle_button(self):
        return self.get_element(self.RECTANGLE_BUTTON_XPATH)

    def rectangle_1_button(self):
        return self.get_element(self.RECTANGLE_1_BUTTON_XPATH)

    def rectangle_2_button(self):
        return self.get_element(self.RECTANGLE_2_BUTTON_XPATH)

    def rectangle_3_button(self):
        return self.get_element(self.RECTANGLE_3_BUTTON_XPATH)

    def polygon_button(self):
        return self.get_element(self.POLYGON_BUTTON_XPATH)

    def circle_button(self):
        return self.get_element(self.CIRCLE_BUTTON_XPATH)

    def circle_1_button(self):
        return self.get_element(self.CIRCLE_1_BUTTON_XPATH)

    def circle_2_button(self):
        return self.get_element(self.CIRCLE_2_BUTTON_XPATH)

    def circle_3_button(self):
        return self.get_element(self.CIRCLE_3_BUTTON_XPATH)

    def wall_button(self):
        return self.get_element(self.WALL_BUTTON_XPATH)

    def boolean_button(self):
        return self.get_element(self.BOOLEAN_BUTTON_XPATH)
