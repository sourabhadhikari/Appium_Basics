from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage = 'in.amazon.mShop.android.shopping',
    appActivity ='com.amazon.mShop.navigation.MainActivity'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
time.sleep(3)
driver.quit()