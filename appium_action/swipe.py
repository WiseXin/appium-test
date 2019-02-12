from time import sleep

from appium_test.find_element.Capabilities import driver


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


size = get_size()
print(size)


# 向左滑动
def swipeleft():
    x1 = int(size[0] * 0.9)
    y1 = int(size[1] * 0.5)
    x2 = int(size[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 500)


# 向左滑动两次
for i in range(2):
    swipeleft()
    sleep(0.5)


# 向上滑动
def swipeup():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)


# 向下滑动
def swipeDown():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.35)
    y2 = int(l[1] * 0.85)
    driver.swipe(x1, y1, x1, y2, 1000)


# 向右滑动
def swipeRight():
    l = get_size()
    y1 = int(l[1] * 0.5)
    x1 = int(l[0] * 0.25)
    x2 = int(l[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)
