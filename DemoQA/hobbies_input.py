import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to wait for element to be clickable
def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

# Initialize WebDriver
chrome_driver_path = "H:\Interactive-Cares-Task\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the website containing the checkbox field
driver.get("https://demoqa.com/automation-practice-form")

try:
    checkbox1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-1']")))
    checkbox1.click()
    time.sleep(2)

    checkbox2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-2']")))
    checkbox2.click()
    time.sleep(2)

    checkbox3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-3']")))
    checkbox3.click()
    time.sleep(2)

    music_checkbox_locator = driver.find_element(By.ID, "hobbies-checkbox-3")
    sports_checkbox_locator = driver.find_element(By.ID, "hobbies-checkbox-1")
    reading_checkbox_locator = driver.find_element(By.ID, "hobbies-checkbox-2")

    # Verify if checkboxes are selected
    all_checkboxes = [sports_checkbox_locator, music_checkbox_locator, reading_checkbox_locator]
    all_selected = all(check_box.is_selected() for check_box in all_checkboxes)

    if all_selected:
        print("All options selected successfully")
    else:
        print("Error: Failed to select all options")

finally:
    # Close the browser
    driver.quit()
