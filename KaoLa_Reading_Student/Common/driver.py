from appium import  webdriver
import yaml
import os



# 读取测试设备配置文件
DevicesFilesPath = os.path.join(os.path.dirname(os.path.dirname(__file__)),"ConfigFiles","DevicesFiles.yaml")
with open(DevicesFilesPath, "r") as DF:
    devicesdata = yaml.load(DF)



def appium_desired():
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",devicesdata)
    return driver


