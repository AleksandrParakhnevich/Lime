import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    close_button = "//button[@class='IButton IButtonClose']"
    menu = "/html/body/div[1]/div/div/div[4]/div[1]/div[1]"
    mans = "//*[@id='app']/div[1]/div/div/div/nav/div/span[2]"
    t_short = "//*[@id='app']/div[1]/div/div/div/nav/ul/li[9]/span"
    all_model = "//*[@id='app']/div[1]/div/div/div/nav/ul/li[9]/ul/li[1]/a"
    filter_button = "//span[@class='filter-button__title']"
    checkbox_1 = "//*[@id='app']/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/label/span[1]"
    checkbox_2 = "/html/body/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/label/span[1]"
    checkbox_3 = "//*[@id='app']/div[1]/div/div/div/div[2]/div/div[3]/div[2]/div[1]/div/label/span[1]"
    close_button_2 = "//button[@class='IButton IButtonClose']"
    product_1 = "//*[@id='app']/div[7]/div/div/div[1]/div[1]/div[3]/div[2]"
    color_1 = "//*[@id='app']/div[7]/div[2]/div/div/div[1]/div[2]/div/div[4]/div[2]/div/div/div[2]/div/img"
    add_cart = "//button[@class='btn btn-cart']"
    cart = "//*[@id='AppNavbar']/div[2]/a[3]"

    # Getters

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.close_button)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.menu)))

    def get_mans(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.mans)))

    def get_t_short(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.t_short)))

    def get_all_model(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.all_model)))

    def get_filter_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_button)))

    def get_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkbox_1)))

    def get_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkbox_2)))

    def get_checkbox_3(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.checkbox_3)))

    def get_close_button_2(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.close_button_2)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_color_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.color_1)))

    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.add_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_close_button(self):
        self.get_close_button().click()
        print("Click close button")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_mans(self):
        self.get_mans().click()
        print("Click mans")

    def click_t_short(self):
        self.get_t_short().click()
        print("Click t_short")

    def click_all_model(self):
        self.get_all_model().click()
        print("Click all model")

    def click_filter_button(self):
        self.get_filter_button().click()
        print("Click filter button")

    def click_checkbox_1(self):
        self.get_checkbox_1().click()
        print("Click checkbox 1")

    def click_checkbox_2(self):
        self.get_checkbox_2().click()
        print("Click checkbox 2")

    def click_checkbox_3(self):
        self.get_checkbox_3().click()
        print("Click checkbox 3")

    def click_close_button_2(self):
        self.get_close_button_2().click()
        print("Click close button 2")

    def click_product_1(self):
        self.get_product_1().click()
        print("Click product 1")

    def click_color_1(self):
        self.get_color_1().click()
        print("Click color 1")

    def click_add_cart(self):
        self.get_add_cart().click()
        print("Click add cart")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # Methods

    def select_product(self):
        self.click_close_button()
        time.sleep(3)
        self.click_menu()
        self.click_mans()
        self.click_t_short()
        self.click_all_model()
        self.click_filter_button()
        self.click_checkbox_1()
        self.click_checkbox_2()
        self.click_checkbox_3()
        self.click_close_button_2()
        self.click_product_1()
        self.click_color_1()
        self.click_add_cart()
        self.click_cart()
        time.sleep(5)
