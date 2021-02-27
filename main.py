# coding=gbk

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait  # �������Եȴ��İ�
from selenium.webdriver.support import expected_conditions as EC  # �ж�����Ҫ��Ԫ���Ƿ��Ѿ������س���
from selenium.webdriver.common.by import By  # ��λ
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

# time.sleep(3)  # ǿ�Ƶȴ�
# el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")

# �ж�ĳ��Ԫ���Ƿ���ӵ���dom�ﲢ�ҿɼ����ɼ�����Ԫ�ؿ���ʾ�ҿ�͸߶�����0
# el2 = WebDriverWait(driver, 10).until(
# 	EC.visibility_of_element_located((By.ID,'com.android.packageinstaller:id/permission_allow_button')))

# �ж�ĳ��Ԫ���Ƿ񱻼ӵ���dom������������Ԫ��һ���ɼ��������λ���ͷ���WebElement
# el2 = WebDriverWait(driver, 10).until(
# 	EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))

	TouchAction(driver).press(x=665, y=1296).move_to(x=667, y=719).release().perform()

el1 = driver.find_element_by_id("com.sgb.management:id/tv_pwd_btn")
el1.click()
el2 = driver.find_element_by_id("com.sgb.management:id/et_pwd_mobile")
el2.send_keys(input('�������ֻ�����:'))
# el2.send_keys('18710512504')

el3 = driver.find_element_by_id("com.sgb.management:id/et_pwd")
el3.click()
el3.send_keys(input('����������:'))
# el3.send_keys('Z5708007Hl')

el4 = driver.find_element_by_id("com.sgb.management:id/tv_pwd_login_btn")
el4.click()

time.sleep(5)

# ��������Ӧ�ó���
driver.start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")

# �����ǰӦ�õİ���
print(driver.current_package)
# �����ǰӦ�õĽ�����
print(driver.current_activity)
# driver.quit()

end = time.perf_counter()
print('Running time: %s Seconds' % (end - start))
