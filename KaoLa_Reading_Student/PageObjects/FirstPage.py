from selenium.webdriver.common.by import By
from  Common.driver import appium_desired
from Common .common_functions import common
from PageObjects.StartPage import startPage
import time


class FirstPage(startPage):
    registerForNewUserElement = (By.ID,"com.koalareading.koalareading:id/tv_register")
    loginForOrdUserElement = (By.ID,"com.koalareading.koalareading:id/tv_login")

    def __init__(self,driver):
        self.driver = driver

    def skip_StartPage(self):
        time.sleep(3)
        self.swipe_left()
        time.sleep(3)
        self.swipe_left()
        time.sleep(3)
        self.swipe_left()
        time.sleep(3)
        self.swipe_left()
        time.sleep(4)
        self.click_ExperienceButten()

    def click_Login_For_Ord_User(self):
        self.findelemnet(*self.registerForNewUserElement).click()

    def click_Register_For_New_User(self):
        self.findelemnet(*self.loginForOrdUserElement).click()


#
#
# if __name__ == '__main__':
#     driver = appium_desired()
#     skip = FirstPage(driver)
#     skip.skip_StartPage()
#     time.sleep(4)
#     skip.click_Login_For_Ord_User()
#
















