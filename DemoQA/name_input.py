import time
import logging
from selenium.webdriver.common.by import By


def name_input_field_validation(driver, test_names):
    try:
        for idx, (first_name, last_name, is_valid) in enumerate(test_names):
            print(f"Running name input validation test with values: {first_name}, {last_name}")

            # Find input fields
            first_name_input = driver.find_element(By.ID, "firstName")
            last_name_input = driver.find_element(By.ID, "lastName")

            # Input test data
            first_name_input.clear()
            last_name_input.clear()
            first_name_input.send_keys(first_name)
            last_name_input.send_keys(last_name)

            # Error message should be displayed for invalid name input
            first_name_error_displayed = None
            last_name_error_displayed = None

            if is_valid and (not first_name_error_displayed and not last_name_error_displayed):
                print('SUCCESS: No error message for valid input')
            elif is_valid and (first_name_error_displayed or last_name_error_displayed):
                print('FAILED: No error message expected for valid input')
            elif not is_valid and (not first_name_error_displayed or not last_name_error_displayed):
                print('FAILED: Error message expected for invalid input')
            else:
                print('SUCCESS: Error message displayed for invalid input')

            time.sleep(2)
    except Exception as e:
        print('ERROR: Error while validating name input field.', e)
