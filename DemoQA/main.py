import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from email_input import email_input_field_validation
from name_input import name_input_field_validation
from gender_input import gender_input_field_validation
from mobile_input import mobile_input_field_validation
from dob_input import dob_input_field_validation
from hobbies_input import hobbies_input_field_validation
from picture_input import picture_input_field_validation
from address_input import address_input_field_validation
from state_and_city import state_input_field_validation

# import test data
from testdata.data import test_emails, test_names, test_genders, test_mobiles, test_dates, test_pictures, test_states

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


chrome_driver_path = "H:\Interactive-Cares-Task\chromedriver.exe"

# Set ChromeDriver path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the website
driver.get("https://demoqa.com/automation-practice-form")

gender_inputs = [
    ("male", False),    # Valid input: Selecting 'male'
    ("female", False),  # Valid input: Selecting 'female'
    ("others", False),  # Valid input: Selecting 'others'
    ("male", True),     # Invalid input: Attempt to select multiple options
    ("female", True),   # Invalid input: Attempt to select multiple options
    ("others", True),   # Invalid input: Attempt to select multiple options
]

# Function to run the tests for gender radio buttons
def run_gender_radio_tests(driver):
    for idx, (selected_option, is_invalid) in enumerate(gender_inputs):
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
        if is_invalid and is_multiple_selected:
            print("Test failed: Multiple options are selected for invalid input")
        elif is_invalid:
            print("Test passed: Invalid input handled correctly")
        elif not is_invalid and is_multiple_selected:
            print("Test failed: Multiple options selected for valid input")
        else:
            print("Test passed: Valid input handled correctly")


try:
    name_input_field_validation(driver, test_names)
    email_input_field_validation(driver, test_emails)
    gender_input_field_validation(driver, test_genders)
    mobile_input_field_validation(driver, test_mobiles)
    dob_input_field_validation(driver, test_dates)
    hobbies_input_field_validation(driver)
    picture_input_field_validation(driver, test_pictures)
    address_input_field_validation(driver)
    state_input_field_validation(driver, test_states)
finally:
    driver.quit()



