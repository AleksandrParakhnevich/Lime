import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class ClientInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    radio_button_1 = "/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div[2]/div/div/div/div/div[4]/div[1]/div[2]/span[1]"
    radio_button_2 = "/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div[2]/div/div/div/div[3]/div/div[3]/span"
    number = "/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[2]/div/form/div[3]/div[2]/div[1]/div[2]/div/input"
    sum = "//input[@id='cert-amount']"
    promo = "/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[2]/div/form/div[4]/div[2]/div/div/input"

    # Getters

    def get_radio_button_1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.radio_button_1)))

    def get_radio_button_2(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.radio_button_2)))

    def get_number(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.number)))

    def get_sum(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.sum)))

    def get_promo(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.promo)))

    # Actions

    def click_radio_button_1(self):
        self.get_radio_button_1().click()
        print("Click radio button 1")

    def click_radio_button_2(self):
        self.get_radio_button_2().click()
        print("Click radio button 2")

    def input_number(self, number):
        self.get_number().send_keys(number)
        print("Input number")

    def input_sum(self, sum):
        self.get_sum().send_keys(sum)
        print("Input sum")

    def input_promo(self, promo):
        self.get_promo().send_keys(promo)
        print("Input promo")

    # Methods

    def input_info(self):
        self.click_radio_button_1()
        time.sleep(2)
        self.click_radio_button_2()
        time.sleep(2)
        self.input_number("2222222222222222")
        time.sleep(1)
        self.input_sum("1000")
        time.sleep(1)
        self.input_promo("ggwp")
