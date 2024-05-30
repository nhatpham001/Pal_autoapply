from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
cService = webdriver.ChromeService(executable_path='C:\Program Files (x86)\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get("https://webapps2.uc.edu/elce/Student")

# Log in actions
usernamebar = driver.find_element(By.ID, "username")
passwordbar = driver.find_element(By.ID, "password")

#Enter your username and password as values of creds
creds = {"username": "username", "password": "username"}

# Username
usernamebar.send_keys(creds["username"])
# Password
passwordbar.send_keys(creds["password"])
# Submit login form
passwordbar.send_keys(Keys.RETURN)

# Wait for user to log in manually
input("Log in and go to View/Rank/Finalize and press ENTER to Continue...")

job_title = {}

# Wait for the tbody element to be present in the DOM
tbody = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "tbody"))
)

continuee = True
job_count = 0

while continuee:
    input("press ENTER to start or Go to the next page ... then press Enter to CONTINUE")

    # Locate elements with <a> tags that have href attributes within the tbody
    a_elements = tbody.find_elements(By.XPATH, ".//a[@href]")

    for a in a_elements:
        href = a.get_attribute("href")
        title = a.get_attribute("aria-label")
        job_title[title] = href
        driver.execute_script(f"window.open('{href}', '_blank');")
        
        driver.switch_to.window(driver.window_handles[-1])
        print("Opened new tab")

        # Interact with the new tab
        try:
            print("Trying to process in new tab ...")
            # Wait for the buttons to be present in the new tab
            buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "RadioButton"))
            )
            print("Found RadioButton elements")

            very_interested_button = driver.find_element(By.ID, "PositionRankId_2")
            save_button = driver.find_element(By.ID, "saveButton")
            
            # actions execution
            driver.execute_script("arguments[0].click();", very_interested_button)
            driver.execute_script("arguments[0].click();", save_button)
            
            print("Finished interacting")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            job_count += 1
            input(f"Done ranking job #{job_count} ...")

    # Ask if the user wants to continue to the next page
    next_page = input("Do you want to continue? y/n")
    if next_page.lower() != "y":
        continuee = False
    else:
        # Re-fetch the tbody after user navigates to the next page
        tbody = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "tbody"))
        )

# Pause to keep the browser open
input("Press Enter to close the browser...")

driver.quit()