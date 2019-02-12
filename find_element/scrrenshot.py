from appium_test.find_element.Capabilities import driver

# 屏幕截图

et_name = driver.find_element_by_id('login_email_edittext')
et_name.clear()
et_name.send_keys('name74269')
driver.find_element_by_id('login_password_edittext').send_keys('pwd59011')
driver.find_element_by_id('login_login_btn').click()

# 屏幕截图方法
driver.save_screenshot('login.png')
driver.get_screenshot_as_file('./images/login.png')
