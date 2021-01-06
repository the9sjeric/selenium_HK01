import json
from time import sleep
from selenium import webdriver

class TestWechatlogin():

    def setup(self):
        #指定使用chrome浏览器登陆
        self.driver = webdriver.Chrome()
        #指定隐式等待10秒
        self.driver.implicitly_wait(10)

    def teardown(self):
        #测试结束后关闭进程，回收资源
        self.driver.quit()

    def test_cookielogin(self):
        ## 首先登录一次企业微信，扫码登录等待时间10秒，用于生成cookie文件。
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # sleep(10)
        ## 将生成的cookie内容导入wechatcookie.json文件保存在当前目录下。
        # wechatcookie  = self.driver.get_cookies()
        # with open("wechatcookie.json", "w") as file:
        #     json.dump(wechatcookie, file)

        # 进入企业微信主页
        self.driver.get("https://work.weixin.qq.com/")
        # 读取上面准备的cookie文件
        with open("wechatcookie.json", "r") as input:
                logincookies = json.load(input)
        # 将读取的cookie内容加入到chromedriver中
        for logincookie in logincookies:
            self.driver.add_cookie(logincookie)
        # 找到"企业登录"按钮并点击
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[2]/aside/a[1]").click()
        sleep(2)
        # 找到"通信录"并点击
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(2)
        # 关闭浏览器页面
        self.driver.close()