from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(executable_path='chromedriver.exe')

#get直接返回，不再等待界面加载完成
driver.get("xxx.xxx")
