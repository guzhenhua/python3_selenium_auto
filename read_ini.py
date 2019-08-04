import configparser
cf=configparser.ConfigParser()
cf.read("E:\gu_python3_selenium\LocalElement.ini")
string=cf.get("RegisterElement","user_email")
print(string.split("<")[1])