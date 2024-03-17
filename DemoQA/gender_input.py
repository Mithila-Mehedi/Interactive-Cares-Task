from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time


def gender_input_field_validation(driver, test_gender):
    try:
        for idx, (selected_option) in enumerate(test_gender):
            print(f"Running test case {idx + 1} with selected option: {selected_option}")

            # Find gender radio buttons
            male_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
            female_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")
            others_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-3']")

            # Clear previous selections (if any)
            male_radio.click()
            female_radio.click()
            others_radio.click()

            # Select the desired option
            if selected_option == "male":
                male_radio.click()
            elif selected_option == "female":
                female_radio.click()
            elif selected_option == "others":
                others_radio.click()

            # Wait a moment to ensure the selection is registered
            time.sleep(1)

            # Check if multiple options are selected
            is_multiple_selected = any([male_radio.is_selected(), female_radio.is_selected(), others_radio.is_selected()])

            # Determine test result
            if is_multiple_selected:
                print("Test failed: Multiple options are selected for invalid input")
            else:
                print("Test passed: Valid input handled correctly")
    except:
        print('Handle exception')
