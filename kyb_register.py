import random

from appium_test.Capabilities import driver

# 进入注册界面
driver.find_element_by_id('login_register_text').click()
# 设置头像
root_element = driver.find_element_by_id('activity_register_parentlayout')
root_element.find_element_by_class_name('android.widget.ImageView').click()
images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
images[3].click()
driver.find_element_by_id('save').click()

# 注册信息填写

username = 'name' + str(random.randint(10000, 99999))
print('username:%s', username)
driver.find_element_by_id('activity_register_username_edittext').send_keys(username)

password = 'pwd' + str(random.randint(10000, 99999))
print('password:%s', password)
driver.find_element_by_id('activity_register_password_edittext').send_keys(password)

email = 'email' + str(random.randint(10000, 99999)) + '@163.com'
print('email:%s', email)
driver.find_element_by_id('activity_register_email_edittext').send_keys(email)

driver.find_element_by_id('activity_register_register_btn').click()

# 院校选择
driver.find_element_by_id('perfectinfomation_edit_school_name').click()
# 选择省份
driver.find_elements_by_id('more_forum_title')[1].click()
# 具体院校-选择同济大学
driver.find_elements_by_id('university_search_item_name')[1].click()

# 专业选择
driver.find_element_by_id('activity_perfectinfomation_major').click()
# 选择经济学类 - 统计学 -经济统计学
driver.find_elements_by_id('major_subject_title')[1].click()
driver.find_elements_by_id('major_group_title')[2].click()
driver.find_elements_by_id('major_search_item_name')[1].click()

# 点击进入考研帮
driver.find_element_by_id('activity_perfectinfomation_goBtn').click()
