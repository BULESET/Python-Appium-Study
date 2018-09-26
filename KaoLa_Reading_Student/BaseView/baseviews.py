


class BaseView():
    def __init__(self,driver):
        self.driver =driver

    def findelemnet(self,*loc):
        return self.driver.find_element(*loc)

    def findelements(self,*locs):
        return self.driver.find_elements(*locs)

