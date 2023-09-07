import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class LoginPage(Base):
    url = 'https://lime-shop.com/ru_ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    auth = "//*[@id='AppNavbar']/div[2]/a[1]"
    auth_button = "//button[@class='btn btn-block btn-outline btn-primary']"
    user_name = "//input[@tabindex='1']"
    password = "//input[@tabindex='2']"
    login_button = "//button[@type='submit']"
    main_word = "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/h1"

    # Getters

    def get_auth(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.auth)))

    def get_auth_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.auth_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_auth(self):
        self.get_auth().click()
        print("Click auth")

    def click_auth_button(self):
        self.get_auth_button().click()
        print("Click auth button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_auth()
        self.click_auth_button()
        self.input_user_name("jin654@yandex.ru")
        self.input_password("52555155")
        self.click_login_button()
        time.sleep(3)
        self.assert_word(self.get_main_word(), "ЛИЧНЫЙ КАБИНЕТ")
        time.sleep(3)
