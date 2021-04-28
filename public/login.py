import time

class allLogin(object):
    def __init__(self, driver):
        self.driver = driver

    def yonghulogin(self):
        self.driver.find_element_by_id("com.wuye:id/phone").clear()
        self.driver.find_element_by_id("com.wuye:id/password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/phone").send_keys("15716550311")
        self.driver.find_element_by_id("com.wuye:id/password").send_keys("123456")
        self.driver.find_element_by_id("com.wuye:id/login_btn").click()
        time.sleep(3)



