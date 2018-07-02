from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options

response = requests.get('https://www.douban.com/misc/captcha?id=U2swbkZjEAwp7XYjwuPeSVZC:en&size=s')
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver = webdriver.Chrome("D:\\chromedriver_win32\\chromedriver.exe")   //地址
#driver = webdriver.Chrome()
driver.get("http://www.douban.com/")
cookies_list = driver.get_cookies()
driver.find_element_by_name('form_email').send_keys('738758058@qq.com')
driver.find_element_by_name('from_password').send_keys('douban789')
