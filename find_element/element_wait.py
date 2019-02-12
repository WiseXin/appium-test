from selenium.webdriver.support.wait import WebDriverWait

from appium_test.find_element.kyb_login import driver

# 元素等待
WebDriverWait(driver, 3, 1).until(lambda x: x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum'),
                                  '正在等待元素出现')
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()
