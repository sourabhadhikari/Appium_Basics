from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy

desired_caps = dict(
    deviceName = 'Android',
browserName = 'Chrome',    platformName = 'Android',
    
    platformVersion = "12.0",
    chromedriverExecutable = 'C:/Users/admin/Desktop/QA_Automation/chromedriver-2.exe'
)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

driver.get('https://google.com')
print(driver.title)
driver.find_element(MobileBy.XPATH,"//*[@name='q']").send_keys('hello')
driver.press_keycode(66)
time.sleep(2)
driver.quit()
