from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

chrome_driver_path=r'chromedriver.exe'
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension("buster.crx")
driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
pageurl = "https://www.kooapp.com/"
# executable_path=r'chromedriver_win32\chromedriver.exe'


# navigate to the Chrome extensions page
driver.get(pageurl)
time.sleep(2)
# click to the login button  //*[@id="mainHeader"]/div/div[2]/ul/button
driver.find_element(By.CLASS_NAME, 'Header_loginBtn__gu5Jl').click() 
driver.implicitly_wait(2)

# //*[@id="modal-root"]/div[2]/div/div[3]/div[3]/button //*[@id="modal-root"]/div[2]/div/div[3]/div[3]/button[2]
# click to sign with email button
try:
    sign_with_email = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div[3]/div[3]/button[2]')
    time.sleep(2)
except NoSuchElementException:
    sign_with_email = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div[3]/div[3]/button')
    time.sleep(2)
sign_with_email.click()
driver.implicitly_wait(5)

# put the email in input field 
email = 'iamsk84@gmail.com'
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email) 
time.sleep(4)




#//*[@id="modal-root"]/div[2]/div/div[3]/div[2]/div/div/div/iframe 
# switch the  recaptcha iframe
#iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[src*="google.com/recaptcha"]')
iframe = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div[3]/div[2]/div/div/div/iframe')
driver.switch_to.frame(iframe)

driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()
driver.implicitly_wait(5)

# Switch back to the default content
driver.switch_to.default_content()
driver.get_screenshot_as_file('8.png')
# switch the  recaptcha challenge iframe
iframe = driver.find_element(By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')
driver.switch_to.frame(iframe)

# click to the buster extension button icon on iframe recaptcha challange
driver.find_element(By.XPATH,'//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]').click()
time.sleep(4)
#driver.find_element(By.XPATH,'/*[@id="recaptcha-verify-button"]').click()
#time.sleep(5)
driver.get_screenshot_as_file('9.png')
# Switch back to the default content
driver.switch_to.default_content()
time.sleep(8)
driver.get_screenshot_as_file('10.png')
# click to get otp / submit button
driver.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div/div[3]/button').click()
time.sleep(5)

# Enter the OTP in input field

#otp =""
OTP = int(input("Enter the OTP code: "))
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="otp"]').send_keys(OTP) 
time.sleep(10)

# click to verify button #Login_verifyBtn__Hs7YX
driver.find_element(By.CLASS_NAME, 'Login_verifyBtn__Hs7YX').click()
time.sleep(4)

print('Bypassing the reCaptcha')
time.sleep(4)