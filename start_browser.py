from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
from PIL import Image
from ShowapiRequest import ShowapiRequest
# driver=webdriver.Chrome()
# # driver=webdriver.edge()
# driver.get("http://www.5itest.cn/register")
# time.sleep(3)
# print(EC.title_contains("注册"))
# # element=driver.find_element_by_id("register_email").send_keys("707016185@qq.com")
# locater=(By.ID,"register_email")
# WebDriverWait(driver,10).until(EC.invisibility_of_element_located(locater))
# driver.find_element_by_id("register_nickname").send_keys("guzhenhua")
# driver.find_element_by_id("register_password").send_keys("123456")
# driver.find_element_by_id("captcha_code").send_keys("5556")
# # EC.invisibility_of_element_located()  判断元素是否可见 结合webdriverwait
# # EC.presence_of_element_located() 判断元素是否在dom中存在
# driver.quit()

# 2-10 输入注册用户名字及获取用户信息
# driver=webdriver.Chrome()
# driver.get("http://www.5itest.cn/register")
# time.sleep(3)
# element=driver.find_element_by_id("register_email")
# print(element.get_attribute("placeholder"))
# element.send_keys("707016185@qq.com")
# #通过element.get_attribute("value")获取input输入的值
# print(element.get_attribute("value"))

#2-11 如何生成用户名和邮箱
# 通过random生产出随机数，通过join把list转成字符串
# for i in range(5):
#     user_email=''.join(random.sample("1234567890",9))
#     print(user_email+"@qq.com")
#
# # 列表转换成字符串
# list=["zhangsan","lisi","wangwu"]
# print(''.join(list))

# 2-12 如何解决验证码思路
# 1.设置万能验证码
# 2.使用cookie绕过
# 3.识别验证码（今天讲解）
# 思路：
# 1.保存图片，根据图片坐标扣取图片
# 2.解析图片
# 3.输入验证码
# 保存图片，根据图片坐标扣取图片
# driver=webdriver.Chrome()
# driver.get("http://www.5itest.cn/register")
# time.sleep(3)
# driver.maximize_window()
# driver.save_screenshot("E:/screenshot.png")
# code_element=driver.find_element_by_id("getcode_num")
# print(code_element.location) #{"x":123,"y":456}
# left=code_element.location['x']
# top=code_element.location['y']
# right=code_element.size['width']+left
# height=code_element.size['height']+top
# im=Image.open("E:/screenshot.png")
# img=im.crop((left,top,right,height))
# img.save("E:/code_element.png")


r = ShowapiRequest("http://route.showapi.com/184-4","101540","ba8f310cfe3444929f34a3cfcca8ed3e" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", "E:/code_element.png") #文件上传时设置
res = r.post()
time.sleep(1)
text = res.json()['showapi_res_body']['Result']
print(text)
