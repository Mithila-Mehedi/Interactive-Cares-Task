from selenium.webdriver.common.by import By
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Function to run the tests for email input field
def email_input_field_validation(driver, test_emails):
    try:
        for idx, (email, is_valid) in enumerate(test_emails):
            print(f"Running email input validation test with email: {email}")

            email_input = driver.find_element(By.ID, "userEmail")
            email_input.clear()
            email_input.send_keys(email)

            # Find the error message element
            error_message_displayed = None

            # Check if the error message is displayed correctly based on the validity of the input
            if is_valid and not error_message_displayed:
                print('SUCCESS: No error message for valid input')
            elif not is_valid and error_message_displayed:
                print('FAILED: Error message expected for invalid input')
            else:
                print('FAILED: Email input validation failed')

            time.sleep(2)
    except Exception as e:
        print('Error validating email input. ', e)
