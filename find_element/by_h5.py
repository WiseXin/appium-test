from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

desired_caps = {
    "platformName": "android",
    "platformVersion": "5.1.1",
    "deviceName": "Android Emulator",
    "appPackage": "com.wondershare.drfone",
    "appActivity": ".ui.activity.WelcomeActivity",
    "noReset": False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

WebDriverWait(driver, 10).until(
    lambda x: x.find_element_by_id('[OFFICIAL]dr.fone app - Backup and restore data on your mobile'))
context = driver.contexts
print(context)
driver.find_element_by_class_name('android.widget.EditText').send_keys('fsfsf11@163.com')

driver.find_element_by_id('Submit').click()
driver.find_element_by_id('转到上一层级').click()
