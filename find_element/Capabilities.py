from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {
    'platformName': 'android',
    'deviceName': 'android emulator',
    'platforVersion': '5.1.1',
    'app': r'E:\BaiduNetdiskDownload\kaoyan3.1.0.apk',
    'appPackage': 'com.tal.kaoyan',
    'appActivity': '.ui.activity.SplashActivity',
    'automationName': 'uiautomator2',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True,
    # 'appPackage': ' com.guokr.mentor',
    # 'appActivity': '.ui.activity.MainActivity',
    'noReset': False
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


def check_canlebtn():
    print('检查cancelbtn键')
    try:
        canclebtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('cancelbtn取消键不存在')
    else:
        canclebtn.click()


def check_skipbtn():
    print('检查skipbtn键')
    try:
        skipbtn = driver.find_element_by_id('tv_skip')
    except NoSuchElementException:
        print('跳过键不存在')
    else:
        skipbtn.click()


check_canlebtn()
# check_skipbtn()
