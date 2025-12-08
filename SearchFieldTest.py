from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start Chrome (chromedriver must be in the same folder or PATH)
driver = webdriver.Chrome()

# Open page
driver.get("https://www.selenium.dev/") 
driver.maximize_window()

time.sleep(2)

# Click documentation
clickDocumentation = driver.find_element(By.XPATH, "//span[normalize-space()='Documentation']").click()
time.sleep(2)
# Click search field
searchfiled = driver.find_element(By.XPATH, "//span[@class='DocSearch-Button-Placeholder']").click()
time.sleep(2)
# Typed search value
searchPopupField = driver.find_element(By.XPATH, "//input[@id='docsearch-input']")
searchPopupField.send_keys("testing")
time.sleep(2)
# Hit keyboard enter to search typed value
searchPopupField.send_keys(Keys.ENTER)
time.sleep(3)

# Checking if the popup field is visible before typing the value
if searchPopupField is None:
    print("Element not found!")
else:
    print("FOUND the ELEMENT")

# Printing the url address after the successful searching
print("Current page url is >> " + driver.current_url)
afterSearchUrlAddress = driver.current_url

# Printing the custom message to check if search is successful or not via current page url
if driver.current_url == afterSearchUrlAddress:
    print ("Landed on the correct page")
else:
    print("WRONG PAGE - searching didn't work properly")

# #driver.quit()
