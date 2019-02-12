# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

from appium_test.find_element.Capabilities import driver

# toast 弹窗识别
et_name = driver.find_element_by_id('login_email_edittext')
et_name.clear()
et_name.send_keys('555')
driver.find_element_by_id('login_password_edittext').send_keys('555')
driver.find_element_by_id('login_login_btn').click()

error_message = '用户名或密码错误，你还可以尝试1次'
limit_message = '验证失败次数过多'

# message = '//*[@text=\'{}\']'.format(error_message)

# message = '//*[@text="{}"]'.format(limit_message)
message = '//*[contains(@text,"验证失败次数过多")]'

toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
print(toast_element.text)
