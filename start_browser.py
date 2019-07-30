from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
# driver=webdriver.edge()
driver.get("http://www.5itest.cn/register")
time.sleep(3)
print(EC.title_contains("注册"))