# coding=gbk

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait  # 导入显性等待的包
from selenium.webdriver.support import expected_conditions as EC  # 判断所需要的元素是否已经被加载出来
from selenium.webdriver.common.by import By  # 定位
from appium.webdriver.common.touch_action import TouchAction

start = time.perf_counter()

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.2"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.sgb.management"
caps["appActivity"] = "com.sgb.management.view.ui.activity.self.userInfo.VerificationCodeLoginActivity"
caps["ensureWebviewsHavePages"] = True
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# time.sleep(3)  # 强制等待
# el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")

# 判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0
# el2 = WebDriverWait(driver, 10).until(
# 	EC.visibility_of_element_located((By.ID,'com.android.packageinstaller:id/permission_allow_button')))

# 判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement
# el2 = WebDriverWait(driver, 10).until(
# 	EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))

	TouchAction(driver).press(x=665, y=1296).move_to(x=667, y=719).release().perform()

el1 = driver.find_element_by_id("com.sgb.management:id/tv_pwd_btn")
el1.click()
el2 = driver.find_element_by_id("com.sgb.management:id/et_pwd_mobile")
el2.send_keys(input('请输入手机号码:'))
# el2.send_keys('18710512504')

el3 = driver.find_element_by_id("com.sgb.management:id/et_pwd")
el3.click()
el3.send_keys(input('请输入密码:'))
# el3.send_keys('Z5708007Hl')

el4 = driver.find_element_by_id("com.sgb.management:id/tv_pwd_login_btn")
el4.click()

time.sleep(5)

# 启动其他应用程序
driver.start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")

# 输出当前应用的包名
print(driver.current_package)
# 输出当前应用的界面名
print(driver.current_activity)
# driver.quit()

end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))
