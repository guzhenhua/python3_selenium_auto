from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver=webdriver.Chrome()
# 初始化driver
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(2)
#定位元素
def get_element(id):
    element=driver.find_element_by_id(id)
    return element
# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element=driver.find_element_by_id("getcode_num")
    print(code_element.location) #{"x":123,"y":456}
    left=code_element.location['x']
    top=code_element.location['y']
    right=code_element.size['width']+left
    height=code_element.size['height']+top
    im=Image.open(file_name)
    img=im.crop((left,top,right,height))
    img.save(file_name)
#     获取随机数
def get_random():
    user_info=''.join(random.sample("1234567890abcdefg",8))
    return user_info
def image_online(flie_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "101540", "ba8f310cfe3444929f34a3cfcca8ed3e")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", flie_name)  # 文件上传时设置
    res = r.post()
    time.sleep(1)
    text = res.json()['showapi_res_body']['Result']
    return text

def run_mian():
    driver_init()
    user_info=get_random()
    get_element("register_email").send_keys(user_info+"@qq.com")
    get_element("register_nickname").send_keys(user_info)
    get_element("register_password").send_keys("111111")
    file_name="E:/guzhenhua/qer_code.png"
    # E: / screenshot.png
    get_code_image(file_name)
    captcha_code=image_online(file_name)
    get_element("captcha_code").send_keys(captcha_code)
    get_element("register-btn").click()
    time.sleep(3)
    driver.close()
run_mian()

