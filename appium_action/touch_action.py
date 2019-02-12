from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

# 随手记app 九宫格滑动


desired_caps = {
    "platformName": "android",
    "platformVersion": "5.1.1",
    "deviceName": "Android Emulator",
    "appPackage": "com.mymoney",
    "appActivity": ".biz.splash.SplashScreenActivity",
    "app": "E:/BaiduNetdiskDownload/mymoney.apk",
    "noReset": False
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 向左滑动
def swipeleft():
    size = get_size()
    x1 = int(size[0] * 0.9)
    y1 = int(size[1] * 0.5)
    x2 = int(size[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 500)


# 向上滑动
def swipeup():
    size = get_size()
    x1 = int(size[0] * 0.5)
    y1 = int(size[1] * 0.95)
    y2 = int(size[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)


WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.mymoney:id/next_btn'))
# 向左滑动两次
for i in range(2):
    swipeleft()
    sleep(0.5)

# 点击 开启随手记
driver.find_element_by_id('com.mymoney:id/begin_btn').click()

# 点击 更多
WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.mymoney:id/nav_setting_btn'))
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_id('com.mymoney:id/content_container_ly'))
swipeup()
# 点击 高级
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
# 密码保护
driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()
driver.find_element_by_id('com.mymoney:id/security_type_briv').click()
# 手势密码
driver.find_element_by_id('com.mymoney:id/ll_gesture_psd').click()

for i in range(2):
    TouchAction(driver).long_press(x=240, y=232).move_to(x=357, y=234).wait(500) \
        .move_to(x=472, y=349).wait(500) \
        .move_to(x=477, y=472).wait(500) \
        .release().perform()
