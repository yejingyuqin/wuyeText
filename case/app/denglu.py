from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
import unittest
import time
import os
from public.login import allLogin


class dengLu(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        # 重置app数据
        desired_caps["fullReset"] = 'True'  # 清除数据卸载app
        desired_caps["app"] = ("E:/appium/app-debug100.apk")  # 安装app
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Androrid Emulato'
        desired_caps['appPackage'] = 'com.wuye'
        desired_caps['appActivity'] = '.yonghu.LoginActivity'
        # 要输入中文需要增加下面两个参数
        desired_caps['unicodeKeyboard'] = 'True'  # 在手机里装一个unicode输入法
        desired_caps['resetKeyboard'] = 'True'  # 把手机默认输入法设置为appium的输入法
        desired_caps['automationName'] = 'Uiautomator2'  #处理toast
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 打印开始时间+当前系统时间的年月日时分秒形式
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        # 定义一个路径
        filedir = "E:/pycharm/test/wuye/"
        if not os.path.exists(filedir):  # 如果系统中没有这个路径
            os.makedirs(os.path.join('E:/', 'pycharm', 'test', 'wuye'))  # 创建这个路径
        # 打印结束时间+当前系统时间的年月日时分秒形式
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        # 定义了一个命名，就是以路径+年月日时分秒+.png
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)  # 截图并以定义的命名命名
        self.driver.quit()

    def testdengLu_01_01(self):
        '''普通用户账号密码登录'''
        self.driver.implicitly_wait(30)
        allLogin(self.driver).yonghulogin()
        time.sleep(2)
        el=self.driver.find_element_by_id("com.wuye:id/phone")
        self.assertEqual(el.text, "15716550311")

    def testdengLu_01_02(self):
        '''错误账号正确密码登录'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/phone").clear()
        self.driver.find_element_by_id("com.wuye:id/password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/phone").send_keys("15621823564")
        self.driver.find_element_by_id("com.wuye:id/password").send_keys("123456")
        self.driver.find_element_by_id("com.wuye:id/login_btn").click()

        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'用户不存在')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False
        self.assertTrue(duanyan)

    def testdengLu_01_03(self):
        '''正确员工账号登录'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/yuangong_login").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/phone").clear()
        self.driver.find_element_by_id("com.wuye:id/password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/phone").send_keys("15059224492")
        self.driver.find_element_by_id("com.wuye:id/password").send_keys("123456")
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/login_btn").click()
        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'登录成功')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False
        self.assertTrue(duanyan)
    def testdengLu_01_04(self):
        '''非员工非普通用户账号登录'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/yuangong_login").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/phone").clear()
        self.driver.find_element_by_id("com.wuye:id/password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/phone").send_keys("15959224492")
        self.driver.find_element_by_id("com.wuye:id/password").send_keys("123456")
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/login_btn").click()
        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'用户不存在')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False
        self.assertTrue(duanyan)

    def testdengLu_01_05(self):
        '''非员工非普通用户账号登录'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/yuangong_login").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/phone").clear()
        self.driver.find_element_by_id("com.wuye:id/password").clear()
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/phone").send_keys("15716550311")
        self.driver.find_element_by_id("com.wuye:id/password").send_keys("12345678")
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/login_btn").click()
        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'密码错误')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False
        self.assertTrue(duanyan)

    def testdengLu_01_06(self):
        '''点击没有账号去注册，查看跳转'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/go_register").click()
        time.sleep(2)
        el=self.driver.find_element_by_id("com.wuye:id/regist_btn")
        time.sleep(2)
        self.assertEqual(el.is_displayed())

    def testdengLu_01_07(self):
        '''点击工作人员登录，查看跳转'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/yuangong_login").click()
        time.sleep(2)
        el = self.driver.find_element_by_xpath("//*[@text='员工登陆']")
        time.sleep(2)
        self.assertEqual(el.is_displayed())

if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

