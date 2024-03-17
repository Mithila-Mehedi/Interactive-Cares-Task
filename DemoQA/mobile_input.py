import time

from selenium.webdriver.common.by import By
import logging


# Function to run the tests for mobile number input field
def mobile_input_field_validation(driver, test_mobiles):
    for idx, (mobile_number, invalid) in enumerate(test_mobiles):
        logging.info(f"Running mobile number test case {idx + 1} with input {mobile_number}")

        # Find the mobile number input field
        mobile_input = driver.find_element(By.ID, "userNumber")

        # Input mobile number
        mobile_input.clear()
        mobile_input.send_keys(mobile_number)

        # Check for validation error message
        error_message_displayed = None
        try:
            error_message_displayed = driver.find_element(By.ID, 'mobile-error').is_displayed()
        except:
            pass

        # Validate the mobile number input
        if invalid:
            if error_message_displayed:
                print("Test passed: Error message displayed for invalid input")
            else:
                print("Test failed: Error message should be displayed for invalid input")
        else:
            if not error_message_displayed:
                print("Test passed: No error message displayed for valid input")
            else:
                print("Test failed: Error message should not be displayed for valid input")

        time.sleep(1)
