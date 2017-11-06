"""
浏览器接口封装

PhantomJS 的未来：
PhantomJS 的核心开发者之一 Vitaly Slobodin 近日宣布，已辞任 maintainer ，不再维护项目。
Vitaly 发文表示，Chrome 59 将支持 headless 模式，用户最终会转向去使用它。Chrome 比PhantomJS 更快，更稳定，也不会像 PhantomJS 这样疯狂吃内存：
“我看不到  PhantomJS 的未来，作为一个单独的开发者去开发 PhantomJS 2 和 2.5 ，简直就像是一个血腥的地狱。即便是最近发布的 2.5 Beta 版本拥有全新、亮眼的 QtWebKit ，但我依然无法做到真正的支持 3 个平台。我们没有得到其他力量的支持！”

各位虫子们，幸运的是Chrome Headless 出现了。不仅能直接绕过cdn反爬，一些功能为正在探索中。

需要安装chromedriver
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PYSTUDY.randomlib import random_user_agent
from PYSTUDY.oslib import get_os_version, set_env
from PYSTUDY.timelib import sleep


class ChromeBrowser(object):
    """
    浏览器
    """
    def __init__(self, headless=False, proxy=None):
        """
        初始化一个driver
        :param headless: 是否启动无头浏览器，默认为不启动无头浏览器
        :param proxy: 是否使用代理，如果不使用代理请不要改动，如果要用就用下面注释的代理差不多的。
        :param timeout: 设置页面加载时间
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--user-agent=' + random_user_agent())
        if headless:
            options.add_argument('headless')
            options.add_argument('disable-gpu')
        else:
            pass

        self.driver = None
        if proxy:
            # PROXY = "localhost:8080"
            PROXY = proxy
            # Create a copy of desired capabilities object.
            desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
            # Change the proxy properties of that copy.
            desired_capabilities['proxy'] = {
                "httpProxy":PROXY,
                "ftpProxy":PROXY,
                "sslProxy":PROXY,
                "noProxy":None,
                "proxyType":"MANUAL",
                "class":"org.openqa.selenium.Proxy",
                "autodetect":False
            }
            self.driver = webdriver.Chrome(chrome_options=options, desired_capabilities=desired_capabilities)
        else:
            self.driver = webdriver.Chrome(chrome_options=options)
        """
        # 设置页面加载时间
        if self.driver:
            self.driver.set_page_load_timeout(timeout)
        else:
            raise Exception('chrome browser init failed.')
        """

    def close(self):
        self.driver.quit()

    def get(self, url):
        """
        以get方式打开一个链接
        :params url: 链接
        """
        self.driver.get(url)

    def find_element_by_sth(self, sth, v):
        if sth == 'id':
            return self.driver.find_element_by_id(v)
        elif sth == 'name':
            return self.driver.find_element_by_name(v)
        elif sth == 'xpath':
            return self.driver.find_element_by_xpath(v)
        elif sth == 'link_text':
            return self.driver.find_element_by_link_text(v)
        elif sth == 'tag_name':
            return self.driver.find_element_by_tag_name_name(v)

    def find_elements_by_sth(self, sth, v):
        if sth == 'id':
            return self.driver.find_elements_by_id(v)
        elif sth == 'name':
            return self.driver.find_elements_by_name(v)
        elif sth == 'xpath':
            return self.driver.find_elements_by_xpath(v)
        elif sth == 'link_text':
            return self.driver.find_elements_by_link_text(v)
        elif sth == 'tag_name':
            return self.driver.find_elements_by_tag_name_name(v)


    def input_send_keys(self, element, keys):
        element.send_keys(keys)

    def input_clear(self, element):
        element.clear()
    
    def submit(self, element):
        element.submit()

    def click(self, element):
        ActionChains(self.driver).double_click(element).perform()

    def get_html(self):
        return self.driver.page_source

    def wait(self, t):
        sleep(t)

    def get_cookie(self):
        cookies = {}
        for ele in self.driver.get_cookies():
            cookies[ele['name']] = ele['value']
        return cookies
                        

if __name__ == '__main__':
    b = ChromeBrowser(False)
    b.get('http://localhost:5000') 
    '''
    inputElement = b.find_element_by_sth('id', 'kw')
    b.input_clear(inputElement)
    b.input_send_keys(inputElement, 'python')
    submitButton = b.find_element_by_sth('id', 'su')
    b.click(submitButton)
    b.wait(10)
    '''
    print(b.get_html())
