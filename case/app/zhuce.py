from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.zhuce import Create
from appium import webdriver
import unittest
import time
import os
import random


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

    def testZhuce_01_01(self):
        '''不填写内容点击注册'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/go_register").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/regist_btn").click()
        try:
            toast_loc=(xpath,".//[contains(@text,请输入必选项)]")
            WebDriverWait(20,0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan=True
        except:
            duanyan=False
        self.assertTrue(duanyan)

    def testZhuce_01_02(self):
        '''正常注册账号'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/go_register").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/phone").clear()
        self.driver.find_element_by_id("com.wuye:id/password").clear()
        #填写手机号
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/phone").send_keys(Create(self.driver).create_phone())
        a=self.driver.find_element_by_id("com.wuye:id/phone").text
        #填写密码,确认密码
        self.driver.find_element_by_id("com.wuye:id/password").send_keys("123123")
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/password_again").send_keys(123123)
        time.sleep(1)
        #填写姓名住址
        self.driver.find_element_by_id("com.wuye:id/name").send_keys("姓名")
        self.driver.find_element_by_id("com.wuye:id/address").send_keys("就住这里这里这里")
        time.sleep(1)
        #点击注册
        self.driver.find_element_by_id("com.wuye:id/regist_btn").click()
        time.sleep(3)
        #检查页面是否跳转到个人中心页面，断言
        phone = self.driver.find_element_by_id("com.wuye:id/phone").text
        xingming = self.driver.find_element_by_id("com.wuye:id/name").text
        dizhi = self.driver.find_element_by_id("com.wuye:id/address").text

        self.assertEqual(a, phone)
        self.assertEqual(xingming, "姓名")
        self.assertEqual(dizhi, "就住这里这里这里")

    # def testZhuce_01_03(self):
    #     '''注册两次密码输入不一致'''
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_id("com.wuye:id/go_register").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_id("com.wuye:id/phone").clear()
    #     self.driver.find_element_by_id("com.wuye:id/password").clear()
    #     # 填写手机号
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.wuye:id/phone").send_keys(Create(self.driver).create_phone())
    #     a = self.driver.find_element_by_id("com.wuye:id/phone").text
    #     # 填写密码,确认密码
    #     self.driver.find_element_by_id("com.wuye:id/password").send_keys("123123")
    #     time.sleep(1)
    #     self.driver.find_element_by_id("com.wuye:id/password_again").send_keys(123123)
    #     time.sleep(1)
    #     # 填写姓名住址
    #     self.driver.find_element_by_id("com.wuye:id/name").send_keys("姓名")
    #     self.driver.find_element_by_id("com.wuye:id/address").send_keys("就住这里这里这里")
    #     time.sleep(1)
    #     # 点击注册
    #     self.driver.find_element_by_id("com.wuye:id/regist_btn").click()
    def testZhuce_01_04(self):
        '''点击已有账号去登录'''
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.wuye:id/go_register").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/go_login").click()
        time.sleep(2)
        el=self.driver.find_element_by_xpath('//*[@text="没有账号去注册"]')
        self.assertTrue(el.is_displayed())
if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



