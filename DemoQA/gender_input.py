from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define test cases for gender radio buttons
test_inputs = [
    ("male", False),    # Valid input: Selecting 'male'
    ("female", False),  # Valid input: Selecting 'female'
    ("others", False),  # Valid input: Selecting 'others'
    ("male", True),     # Invalid input: Attempt to select multiple options
    ("female", True),   # Invalid input: Attempt to select multiple options
    ("others", True),   # Invalid input: Attempt to select multiple options
]

# Function to run the tests for gender radio buttons
def run_gender_radio_tests(driver):
    for idx, (selected_option, is_invalid) in enumerate(test_inputs):
        logging.info(f"Running test case {idx + 1} with selected option: {selected_option}")

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

# Set ChromeDriver path
chrome_driver_path = "H:\Interactive-Cares-Task\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the website
driver.get("https://demoqa.com/automation-practice-form")

try:
    # Run gender radio button tests
    run_gender_radio_tests(driver)
finally:
    # Close the browser session
    driver.quit()
