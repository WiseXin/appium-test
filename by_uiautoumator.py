from appium_test.Capabilities import driver

# username:%s name74269
# password:%s pwd59011
name_text = 'new UiSelector().text("请输入用户名")'
driver.find_element_by_android_uiautomator(name_text).send_keys('name74269')
# 组合定位
pwd_id = 'new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext").className("android.widget.EditText")'
driver.find_element_by_android_uiautomator(pwd_id).send_keys('pwd59011')

login = 'new UiSelector().className("android.widget.Button")'
driver.find_element_by_android_uiautomator(login).click()
