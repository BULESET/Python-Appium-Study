
from selenium.webdriver.common.by import By
from Common .common_functions import common
from PageObjects.FirstPage import FirstPage
from PageObjects.StartPage import startPage
from Common.driver import appium_desired
import  time

class LoginPage(FirstPage):
    usenameElement = (By.ID, 'com.koalareading.koalareading:id/et_username')
    passwordElement = (By.ID, 'com.koalareading.koalareading:id/et_pwd')
    LoginButtenElement = (By.ID, 'com.koalareading.koalareading:id/btn_login')
    ForgetPasswrodsButtenElement = (By.ID, 'com.koalareading.koalareading:id/tv_forgetpwd')
    ViewPasswordElement = (By.ID,"com.koalareading.koalareading:id/img_show_pwd")

    usename = ""
    password = ""


    def __init__(self,driver):
        self.driver = driver

    def input_User_Name(self):
        self.findelemnet(*self.usenameElement).clear()
        self.findelemnet(*self.usenameElement).send_keys(self.usename)

    def input_User_Passwrod(self):
        self.findelemnet(*self.passwordElement).clear()
        self.findelemnet(*self.passwordElement).send_keys(self.password)


    def click_Login_Butten(self):
        self.findelemnet(*self.LoginButtenElement).click()

    def click_Forget_Passwrod_Butten(self):
        self.findelemnet(*self.ForgetPasswrodsButtenElement).click()

    def click_View_Password_Butten(self):
        self.findelemnet(*self.ViewPasswordElement).click()

    def skip_FirstPage_Action(self):
        self.skip_StartPage()
        self.click_Login_For_Ord_User()


    def login_Action(self):
        time.sleep(3)
        self.input_User_Name()
        self.input_User_Passwrod()
        self.click_Login_Butten()

    def click_Forget_Password_Butten(self):
        self.click_Forget_Passwrod_Butten()


# if __name__ == '__main__':
#     driver = appium_desired()
#     skip = LoginPage(driver)
#     skip.skip_FirstPage_Action()
#     time.sleep(4)
#     skip.login_Action()
#
#
# #

















