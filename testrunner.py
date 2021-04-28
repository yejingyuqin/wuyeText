import unittest   #导入unittest模块
import time      #导入time  模块
import os,sys   #导入os,sys模块
from report import HTMLTestRunner   #导入HTMLTestRunner模块


# 获取当前py文件路径地址，并进行路径分割（分割成目录路径和文件名称）
#os.path.split是路径分割的一个方法
#定义了两个变量，dirname就是py文件的绝对路径，filename就是testrunner.py文件的名字
dirname,filename=os.path.split(os.path.abspath(sys.argv[0]))
print(dirname,filename)  #打印出来dirname,filename
case_path = ".\\case\\app\\"   #定义了一个case_path变量，就是当前路径下case\web路径
result = dirname+"\\report\\"   #定义了一个result路径，就是py文件的路径连接了report

#定义了一个方法，不调用就不会执行
def Creatsuite():
    #定义单元测试容器
    testunit = unittest.TestSuite()    #初始化了一个unittest模块的TestSuite，TestSuite是一个测试套件

    #定搜索用例文件的方法
    #加载case/web下的所有py文件
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*.py', top_level_dir=None)

    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename) #通过addText方法把所有的test_suite加到testunit中
        #print testunit
    return testunit

test_case = Creatsuite()

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))   #格式化年月日时分秒
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))  #格式化年月日

#定义个报告存放路径，支持相对路径
tdresult = result + day

if os.path.exists(tdresult): # 检验文件夹路径是否已经存在   ，如果当前电脑中存在当前日期的路径
    filename = tdresult + "\\" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试报告',
                                           description='执行情况：')

    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
else:
    os.mkdir(tdresult) # 创建测试报告文件夹   ，创建一个路径
    filename = tdresult + "\\" + now + "_result.html"       #在report文件下放一个年月日十分秒的文件
    fp = open(filename, 'wb')   #以写二进制的形式打开这个文件
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,             #HTML TestRunner是生成html报告的一个模块，需要导入模块
                                             title='Selenium测试报告',       #显示在报告里的名称
                                             description='执行情况：')

    #运行测试用例
    runner.run(test_case)       #运行所有的test_case
    fp.close()  #关闭报告文件