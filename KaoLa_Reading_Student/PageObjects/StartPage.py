from selenium.webdriver.common.by import By
from Common .common_functions import common
from Common.driver import appium_desired
import time


class startPage(common):
    experienceButtenElement = (By.ID,"com.koalareading.koalareading:id/go_main")

    def __init__(self,driver):
        self.driver = driver

    def swipe_StartPage(self):
        self.swipe_left()

    def click_ExperienceButten(self):
        self.findelemnet(*self.experienceButtenElement).click()




