from appium_test.Capabilities import driver

driver.find_element_by_id('login_register_text').click()
root_element = driver.find_element_by_id('activity_register_parentlayout')
root_element.find_element_by_class_name('android.widget.ImageView').click()
