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

    def testgerenZhongxin_01_01(self):
        '''修改地址页面正常修改地址'''
        allLogin(self.driver).yonghulogin()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = "修改地址"]').click()
        time.sleep(3)
        self.driver.find_element_by_id("com.wuye:id/address").clear()  #清空地址
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/address").send_keys("新的地址"+time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        time.sleep(1)
        self.driver.find_element_by_id("com.wuye:id/button").click()   #点击确定
        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'修改成功')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False
        self.assertTrue(duanyan)
    def testgerenZhongxin_01_02(self):
        '''修改地址页面不修改原地址直接提交'''
        allLogin(self.driver).yonghulogin()
        #点击修改地址
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = "修改地址"]').click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/button").click()   #点击确定
        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'地址没有改变')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False

    def testgerenZhongxin_02_01(self):
        '''服务预约不填写直接提交'''
        allLogin(self.driver).yonghulogin()
        # 点击服务预约
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = "服务预约"]').click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/button").click()
        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'保修内容不能为空')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False

    def testgerenZhongxin_02_02(self):
        '''服务预约正确填写提交'''
        allLogin(self.driver).yonghulogin()
        # 点击服务预约
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = "服务预约"]').click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/content").send_keys("这是一个服务预约")
        time.sleep(1)
        #服务时间
        self.driver.find_element_by_id("com.wuye:id/time").send_keys(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        time.sleep(1)
        #选择服务类型
        self.driver.find_element_by_id("com.wuye:id/leixing").click()
        time.sleep(1)
        self.driver.find_elements_by_id("android:id/text1")[3].click()
        time.sleep(1)
        #点击提交
        self.driver.find_element_by_id("com.wuye:id/button").click()
        try:
            # 处理toast方法
            toast_loc = ("xpath", ".//*[contains(@text,'提交成功')]")
            WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
            duanyan = True
        except:
            duanyan = False
    def testgerenZhongxin_02_03(self):
        '''检查已提交的服务预约是否正确显示在待接单页面'''
        allLogin(self.driver).yonghulogin()
        # 点击服务预约
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = "服务预约"]').click()
        time.sleep(2)
        self.driver.find_element_by_id("com.wuye:id/content").send_keys("这是一个服务预约")
        time.sleep(1)
        #服务时间
        self.driver.find_element_by_id("com.wuye:id/time").send_keys(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        shuru=self.driver.find_element_by_id("com.wuye:id/time").text
        time.sleep(1)
        #选择服务类型
        self.driver.find_element_by_id("com.wuye:id/leixing").click()
        time.sleep(1)
        self.driver.find_elements_by_id("android:id/text1")[3].click()
        time.sleep(1)
        #点击提交
        self.driver.find_element_by_id("com.wuye:id/button").click()
        time.sleep(3)
        #进入我的订单页面
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = "我的订单"]').click()
        time.sleep(2)
        el = self.driver.find_elements_by_id("com.wuye:id/tvTime")
        time.sleep(1)
        try:
            self.driver.swipe(500, 1000, 500, 200, 30000)
            yanzheng=(id, "com.wuye:id/tvTime")
            WebDriverWait(300,0.1).until(EC.presence_of_element_located(yanzheng))
            duanyan=True
        except:
            duanyan=False
        self.assertTrue(duanyan)

    def testgerenZhongxin_02_04(self):
        '''点击退出登录'''
        self.driver.implicitly_wait(60)
        allLogin(self.driver).yonghulogin()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@text="退出登录"]').click()
        time.sleep(2)
        el = self.driver.find_element_by_xpath('//*[@text="没有账号去注册"]')
        self.assertTrue(el.is_displayed())

if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)




