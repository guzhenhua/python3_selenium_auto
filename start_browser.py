from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.common.by import By
driver=webdriver.Chrome()
# driver=webdriver.edge()
driver.get("http://www.5itest.cn/register")
time.sleep(3)
print(EC.title_contains("注册"))
# element=driver.find_element_by_id("register_email").send_keys("707016185@qq.com")
locater=(By.ID,"register_email")
WebDriverWait(driver,10).until(EC.invisibility_of_element_located(locater))
driver.find_element_by_id("register_nickname").send_keys("guzhenhua")
driver.find_element_by_id("register_password").send_keys("123456")
driver.find_element_by_id("captcha_code").send_keys("5556")
# EC.invisibility_of_element_located()  判断元素是否可见 结合webdriverwait
# EC.presence_of_element_located() 判断元素是否在dom中存在
driver.quit()