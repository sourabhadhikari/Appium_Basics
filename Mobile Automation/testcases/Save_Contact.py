from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


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
wait = WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException])
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.dialer:id/contacts_tab')))
driver.find_element(MobileBy.ID,'com.android.dialer:id/contacts_tab').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.contacts:id/expansion_view')))
driver.find_element(MobileBy.ID,'com.android.contacts:id/expansion_view').click()
driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]').send_keys('Iyer')
# driver.find_element(MobileBy.ID,'com.android.dialer:id/eight').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/six').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/one').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/nine').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/nine').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/four').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/six').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/two').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/eight').click()
# driver.find_element(MobileBy.ID,'com.android.dialer:id/eight').click()
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