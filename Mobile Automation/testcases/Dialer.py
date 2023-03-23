from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


desired_caps = dict(
    deviceName = 'Android',
    platformName = 'Android',
    # browserName = 'Chrome',
    # platformVersion = "10.0",
    # automationName= 'UiAutomator2',
    # chromedriverExecutable = 'C:/Users/admin/Desktop/QA_Automation/chromedriver.exe',
    # appPackage = 'com.android.contacts',
    # appActivity ='.activities.PeopleActivity'
    appPackage = 'com.android.dialer',
    appActivity ='.main.impl.MainActivity'
    # 'settings[waitForIdleTimeout]'= 100

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
# driver.update_settings({"waitForIdleTimeout","5"})
time.sleep(3)
driver.find_element(MobileBy.ID,'com.android.dialer:id/fab').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/eight').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/six').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/one').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/nine').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/nine').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/four').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/six').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/two').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/eight').click()
driver.find_element(MobileBy.ID,'com.android.dialer:id/eight').click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='eight']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='six']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='one']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='nine']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='nine']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='four']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='six']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='two']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='eight']").click()
# driver.find_element(MobileBy.XPATH,"//android.widget.ImageButton[@content-desc='eight']").click()



# TouchAction(driver).tap(x=408,y=181).perform()

time.sleep(2)
driver.quit()