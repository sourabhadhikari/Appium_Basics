from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.truthordare',
    appActivity='.MainActivity'
)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
driver.implicitly_wait(20)
driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]').click()
time.sleep(5)
# names = driver.find_elements(MobileBy.XPATH,'/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR('new UiSelector.text("Player 1")')).send_keys('Sourabh')


driver.quit()


