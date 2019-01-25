from appium_test.Capabilities import driver, NoSuchElementException


def login():
    et_name = driver.find_element_by_id('login_email_edittext')
    et_name.clear()
    et_name.send_keys('自学网2018')
    driver.find_element_by_id('login_password_edittext').send_keys('zxw2018')
    driver.find_element_by_id('login_login_btn').click()


try:
    driver.find_element_by_id('mainactivity_button_mysefl').click()
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id('activity_usercenter_username').click()
    login()
