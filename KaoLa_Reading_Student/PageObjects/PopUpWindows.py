from PageObjects.LoginPage import LoginPage
from  selenium.webdriver.common.by import By




class popUpWindows(LoginPage):
    # 升级弹窗页面元素
    cancleButtenElement = (By.ID,"com.koalareading.koalareading:id/tv_cancel")
    upDataWindowsElement = (By.ID,"com.koalareading.koalareading:id/tv_download")

    # 每日签到页面元素

    RegistrationCancleButtenElement = (By.ID,"com.koalareading.koalareading:id/img_close")
    GetGoldButtenElement = (By.ID,"com.koalareading.koalareading:id/img_gold_bg")
    GetGoldButtenElementFirstDay = (By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    GetGoldButtenElementSecondDay = (By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    GetGoldButtenElementThirdDay = (By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    GetGoldButtenElementFourthday = (By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    GetGoldButtenElementFifthDay = (By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    GetGoldButtenElementSixthDay = (By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[6]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    GetGoldButtenElementSeventhDay = (By.XPATH,"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]")




    # 作业页面中提示学生作业布置弹窗页面元素
    knownHomeWorkForStudentElement = (By.ID,"com.koalareading.koalareading:id/id_fragment_my_class_work_guide_button")

    def __init__(self,driver):
        self.driver =driver


    def click_Cancel_Butten(self):
        self.findelemnet(*self.cancleButtenElement).click()


    def click_Upgrade_Butten(self):
        self.findelemnet(*self.upDataWindowsElement).click()

    def get_Gold_Fist_Day(self):
        self.findelemnet(*self.GetGoldButtenElementFirstDay).click()

    def get_Gold_Second_Day(self):
        self.findelemnet(*self.GetGoldButtenElementSecondDay).click()

    def get_Gold_Third_Day(self):
        self.findelemnet(*self.GetGoldButtenElementThirdDay).click()


    def get_Gold_Fourth_day(self):
        self.findelemnet(*self.GetGoldButtenElementFourthday).click()

    def get_Gold_Fifth_Day(self):
        self.findelemnet(*self.GetGoldButtenElementFifthDay).click()


    def get_Gold_Sixth_Day(self):
        self.findelemnet(*self.GetGoldButtenElementSixthDay).click()


    def get_Gold_Seventh_Day(self):
        self.findelemnet(*self.GetGoldButtenElementSeventhDay).click()










