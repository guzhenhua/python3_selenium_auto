import configparser
class Read_ini(object):
    def __init__(self,file_name=None,node=None):
        if file_name==None:
            file_name="E:\gu_python3_selenium\LocalElement.ini"
        if node==None:
            node="RegisterElement"
        self.node=node
        self.cf=self.load_ini(file_name)
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf
    def get_value(self,key):
        return  self.cf.get(self.node,key)
if __name__=="__main__":
    read_ini=Read_ini()
    print(read_ini.get_value("user_nickname"))