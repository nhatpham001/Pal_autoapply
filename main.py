from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




cService = webdriver.ChromeService(executable_path='C:\Program Files (x86)\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service = cService)

driver.get("https://webapps2.uc.edu/elce/Student")
actions =  ActionChains(driver)

#log in actions
usernamebar = driver.find_element("id", "username")
passwordbar = driver.find_element("id", "password")

creds = {"username": "phamn2", "password": "Brianna@0422"}
    #username
actions =  ActionChains(driver)
actions.click(usernamebar)

usernamebar.send_keys(creds["username"])
    #password
actions.click(passwordbar)
passwordbar.send_keys(creds["password"])

# log in and go to the right page
input("Log in and go to View/Rank/Finalize ...")

job_title = {}


# Wait for the tbody element to be present in the DOM
tbody = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "tbody"))
)

# Locate elements with <a> tags that have href attributes within the tbody
a_elements = tbody.find_elements(By.XPATH, ".//a[@href]")
continuee = True
job_count = 0
while continuee:
    input("go to the next page ... then press Enter to CONTINUE")

#---------------------------------------------------------
    #open each href link to interact and rank job post
    # Extract and print the URLs from the href attributes
    for a in a_elements:
        href = a.get_attribute("href")

        title = a.get_attribute("aria-label")
        job_title[title] = href
        driver.execute_script(f"window.open('{href}', '_blank');")
        
        driver.switch_to.window(driver.window_handles[-1])
        print("opened new tab")
        # #interact with button
        try:
            print("trying to process in new tab ...")
            buttons =WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "RadioButton"))
            )
            print("trying to interact with new tab")
            very_interested_button = driver.find_element(By.ID, "PositionRankId_2")
            save_button = driver.find_element(By.ID, "saveButton")
            actions.click(very_interested_button).perform()
            actions.click(save_button).perform()
            print("finished interacting")
            # actions.click(save_button)
        except:
            driver.close()
            print("did not finish action on new tab ...")
            pass
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        job_count += 1
        input(f"done ranking job #{job_count} ..........")

#--------------------------------------------------------------------------------------

#going to next page
    next_page = input("Do you want to continue? y/n")
    if next_page == "y":
        continuee = True
    else:
        continuee = False


# Pause to keep the browser open if needed
input("Press Enter to close the browser...")



driver.quit()