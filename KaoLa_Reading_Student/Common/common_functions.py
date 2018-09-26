import zmail
import  os ,time
import yaml
import pymysql
from BaseView.baseviews import BaseView





class common(BaseView):



    def get_windows_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return (x, y)

    def swipe_up(self):
        screen = self.get_windows_size()
        x1 = screen[0] * 0.5
        y1 = screen[1] * 0.75
        x2 = screen[0] * 0.5
        y2 = screen[1] * 0.25
        self.driver.swipe(x1, y1, x2, y2, 180)

    def swipe_left(self):
        screen = self.get_windows_size()
        x1 = screen[0] * 0.75
        y1 = screen[1] * 0.5
        x2 = screen[0] * 0.25
        y2 = screen[1] * 0.5
        self.driver.swipe(x1, y1, x2, y2, 180)


    def swipe_right(self):
        screen = self.get_windows_size()
        x1 = screen[0] * 0.25
        y1 = screen[1] * 0.5
        x2 = screen[0] * 0.75
        y2 = screen[1] * 0.5
        self.driver.swipe(x1, y1, x2, y2, 180)


    def swipe_down(self):
        screen = self.get_windows_size()
        x1 = screen[0] * 0.25
        y1 = screen[1] * 0.5
        x2 = screen[0] * 0.25
        y2 = screen[1] * 0.75
        self.driver.swipe(x1, y1, x2, y2, 180)


    def get_screenshot(self,modlename):
        nowtime = time.strftime("%Y-%m-%d %H_%M_%S")
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/Screenshots/%s_%s.png' % (nowtime, modlename)
        print(image_file)
        self.driver.get_screenshot_as_file(image_file)

class sendEmail():

    def send_Email(self):
        EmailFilesPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ConfigFiles", "EmailFiles.yaml")
        with open(EmailFilesPath, "r", encoding='utf-8') as EF:
            EmailFiels = yaml.load(EF)

        mail = {
            "subject": EmailFiels["subject"],
            "content": EmailFiels["content"]
        }
        server = zmail.server(EmailFiels["sender"], EmailFiels["passwords"])
        server.send_mail(EmailFiels["reservers"], mail)




class SQL():

    SqlFilePath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ConfigFiles", "SQL.yaml")
    with open(SqlFilePath,"r",encoding="utf-8") as SqlFile:
        sql = yaml.load(SqlFile)

    Host = sql["Host"]
    UserName = sql["UserName"]
    DataBase = sql["DataBase"]

    def connectMySql(self):
        self.db = pymysql.connect(self.Host,self.UserName,self.DataBase,charset='utf8')

    def queryMysql(self,querySQL):
        self.cursor = self.db.cursor()
        self.cursor.execute(querySQL)
        self.data = self.cursor.fetchall()
        # print(self.data)
        totleQustions = len(self.data)
        print(totleQustions)
        listquesiton = list(self.data)
        print(listquesiton[0])
        self.db.close()

    # def updataTableMysq(self):
    #     pass
    #
    # def deleteDataMysql(self):
    #     pass
    #
    # def insertMysql(self):
    #     pass
    #
    # def createTableMysql(self):
    #     pass
    #
    # def dropTableMysql(self):
    #     pass
    #
    #
    # def dropDatabaseMysql(self):
    #     pass



A = SQL()
A.connectMySql()
A.queryMysql()



























