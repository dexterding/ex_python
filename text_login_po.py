import time
from appium import  webdriver

class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver

    def input_account(self,name,pwd):
        "根据不同场景采取不同操作，如：验证码登录页时，xxx.默认账号登录页时，xxx"

        if （is_in_vcode_loginpage == True):
            vcode_loginpage(name,pwd)
        if （is_in_default_loginpage == True):
            default_loginpage(name, pwd)

        return
    def vcode_loginpage(self,name,pwd):
        pass

    def is_in_vcode_loginpage(self):
        pass

    def default_loginpage(self,name,pwd):
        pass

    def is_in_default_loginpage(self):
        pass

    def is_login_sucess(self):
        "在此page找到相关元素即可判断登录成功，否则则不成功"
        pass
        return


def test_login(self)):
    login_page = LoginPage(self.driver)
    login_page.input_account(name,pwd)
    assert login_page.is_login_sucess = True
