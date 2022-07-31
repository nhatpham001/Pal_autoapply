from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://webapps2.uc.edu/elce/Student")

#wait time to load in elements
driver.implicitly_wait(5)

#log in actions
usernamebar = driver.find_element("id", "username")
passwordbar = driver.find_element("id", "password")

    #username
actions =  ActionChains(driver)
actions.click(usernamebar)
usernamebar.send_keys("phamn2")
    #password
actions.click(passwordbar)
passwordbar.send_keys("Brianna_0621")
passwordbar.send_keys(Keys.RETURN)

time.sleep(20)
#directing to new page
try:
    viewrankmenu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "viewRankMenuLink")))
    viewrank = driver.find_element("id", "viewRankMenuLink")
    myaccount = driver.find_element("id", "MyAccountMenuLink")
    actions.click(myaccount)

except:
    driver.quit()



time.sleep(1000)
driver.quit()

