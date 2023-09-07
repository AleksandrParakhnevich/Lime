import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    finish_word = "/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/div[2]/div/form/div[4]/div[3]"

    # Getters

    def get_finish_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.finish_word)))

    # Actions

    # Methods

    def finish(self):
        self.get_current_url()
        time.sleep(10)
        self.assert_finish_word(self.get_finish_word(), "промокод не найден")
        time.sleep(1)
        self.get_screenshot()
