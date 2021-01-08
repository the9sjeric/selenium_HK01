import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestWechatlogin():

    def setup(self):
        # 首先进入chrome安装文件夹/Google/Chrome/Application下，使用gitbash运行以下命令
        # ./chrome --remote-debugging-port=9222
        # 启动一个Debug监听端口的浏览器(测试结束前都不能关闭)

        # 设置测试时使用的chromtdriver的相关参数
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        # 指定使用chromedriver并传入参数
        self.driver = webdriver.Chrome(options=chrome_args)
        # 指定隐式等待10秒
        self.driver.implicitly_wait(10)

    def test_cookielogin(self):
        # 登录企业微信首页
        self.driver.get("https://work.weixin.qq.com/")
        # 点击右上角"企业登录"标签
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[2]/aside/a[1]").click()
        sleep(3)
        # 找到"通信录"并点击
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(3)
        # 关闭浏览器页面(当前页面为浏览器最后一个页面时，不会被关闭)
        self.driver.close()