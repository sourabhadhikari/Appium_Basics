from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.infosys.FLVersion',
    appActivity='.FLVersion'
  
)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
wait = WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions=[NoSuchElementException])
# def elementWait (by,locator):
#     return wait.until(EC.presence_of_element_located((MobileBy.by,'locator')))
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_one_time_button')))
driver.find_element(MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_one_time_button').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_one_time_button')))
driver.find_element(MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_one_time_button').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button')))
driver.find_element(MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button')))
driver.find_element(MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button')))
driver.find_element(MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button')))
driver.find_element(MobileBy.ID,'com.android.permissioncontroller:id/permission_allow_button').click()
wait.until(EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Proceed To Login")')))
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Proceed To Login")').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'FinacleUserCorporateId')))
driver.find_element(MobileBy.ID,'FinacleUserCorporateId').send_keys('104232509VVD')
driver.find_element(MobileBy.ID,'mPinLoginButFirstTime').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'appActivation.authenticateOTP')))
driver.find_element(MobileBy.ID,'appActivation.authenticateOTP').send_keys('086697')
driver.find_element(MobileBy.ID,'activationOtpSubmit').click()
wait.until(EC.presence_of_element_located((MobileBy.ID,'appActivation.userMPIN')))
driver.find_element(MobileBy.ID,'appActivation.userMPIN').send_keys('1234')
driver.find_element(MobileBy.ID,'appActivation.confirmMPIN').send_keys('1234')
driver.find_element(MobileBy.ID,'setMPINClick').click()
driver.find_element(MobileBy.ID,'registerChannelCancel').send_keys('1234')
driver.find_element(MobileBy.ID,'registerChannelCancel').click()


	

time.sleep(10)
driver.quit()