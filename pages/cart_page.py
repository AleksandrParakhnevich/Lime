import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    amount = "//div[@class='DropdownList__header']"
    amount_3 = "//*[@id='app']/div[4]/div/div/div[2]/div[1]/div/div[1]/div/div/div[6]/div/div/div[2]/div[3]/span"
    order_button = "//*[@id='app']/div[4]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/button"

    # Getters

    def get_amount(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.amount)))

    def get_amount_3(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.amount_3)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions

    def click_amount(self):
        self.get_amount().click()
        print("Click amount")

    def click_amount_3(self):
        self.get_amount_3().click()
        print("Click amount 3")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order_button")

    # Methods

    def ordering(self):
        self.click_amount()
        self.click_amount_3()
        self.click_order_button()
        time.sleep(2)
