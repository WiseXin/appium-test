from appium_test.find_element.Capabilities import driver

# relative 相对定位 先定位父元素节点，然后基于父元素节点定位
driver.find_element_by_id('login_register_text').click()
root_element = driver.find_element_by_id('activity_register_parentlayout')
# 基于父元素root_element节点定位
root_element.find_element_by_class_name('android.widget.ImageView').click()
