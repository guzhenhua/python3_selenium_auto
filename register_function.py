from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest
from PIL import Image
from find_element import FindElement

class RegiterFunction(object):
    def __init__(self,url):
        self.driver=self.get_driver(url)
    #     初始化driver
    def get_driver(self,url):
        driver=webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver
    # 输入用户信息
    def send_user_info(self,key,data):
        self.get_element(key).send_keys(data)
    #定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        return find_element.get_element(key)
    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        print(code_element.location)  # {"x":123,"y":456}
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    #     获取随机数
    def get_random(self):
        user_info = ''.join(random.sample("1234567890abcdefg", 8))
        return user_info

    def image_online(self,flie_name):
        self.get_code_image(flie_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "101540", "ba8f310cfe3444929f34a3cfcca8ed3e")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", flie_name)  # 文件上传时设置
        res = r.post()
        time.sleep(1)
        text = res.json()['showapi_res_body']['Result']
        return text

def run_mian():
        register_function=RegiterFunction("http://www.5itest.cn/register")
        user_info_random = register_function.get_random()
        register_function.send_user_info("user_email",user_info_random + "@qq.com")
        register_function.send_user_info("user_nickname",user_info_random)
        register_function.send_user_info("user_password","111111")
        file_name = "E:/guzhenhua/qer_code.png"
        # E: / screenshot.png
        captcha_code = register_function.image_online(file_name)
        register_function.send_user_info("user_captcha_code",captcha_code)
        register_function.get_element("user_register_btn").click()
        code_text=register_function.get_element("user_captcha_code_error")
        if (code_text==None):
            print("执行成功")
        else:
            register_function.driver.save_screenshot("E:/guzhenhua/code_error.png")
            print("执行失败")
        time.sleep(3)
        register_function.driver.close()
if __name__=="__main__":
    run_mian()
