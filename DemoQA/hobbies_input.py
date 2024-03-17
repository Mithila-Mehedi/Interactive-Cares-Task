import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def hobbies_input_field_validation(driver):
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
    except:
        print('Handle this error')
