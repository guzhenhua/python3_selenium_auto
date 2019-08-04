from util.read_ini import Read_ini
class FindElement(object):
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,key):
        read_ini=Read_ini()
        by=read_ini.get_value(key).split("<")[1]
        local=read_ini.get_value(key).split("<")[0]
        if by=="id":
            return self.driver.find_element_by_id(local)
        if by == "xpath":
            return self.driver.find_element_by_Xpath(local)