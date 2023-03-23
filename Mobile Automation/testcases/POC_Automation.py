from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.moonraft.pnbcorp',
    appActivity='.MainActivity',
    browserName = 'Chrome'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

driver.find_element(MobileBy.ID,"com.android.permissioncontroller:id/permission_allow_button").click()

time.sleep(100)
driver.quit()