import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define valid picture file formats
VALID_FILE_FORMATS = ["png", "jpeg", "jpg"]

# Define test inputs with file paths
test_inputs = {
    "valid_picture": "valid_file.png",
    "invalid_picture": "invalid_file.pdf"
}

# Initialize WebDriver
chrome_driver_path = "H:\Interactive-Cares-Task\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the website containing the form
driver.get("https://demoqa.com/automation-practice-form")

try:
    for test_case, file_path in test_inputs.items():
        # Find the file input field
        file_input = driver.find_element(By.ID, "uploadPicture")

        file_input.clear()

        current_dir = os.getcwd()
        path = os.path.join(current_dir, 'assets', file_path)
        print('File path: ', path)
        file_input.send_keys(path)
        time.sleep(3)

        # Check if the uploaded file format is valid
        uploaded_file_name = file_input.get_attribute("value")
        file_extension = uploaded_file_name.split(".")[-1].lower()

        if file_extension in VALID_FILE_FORMATS:
            print(f"Test passed: {test_case} - File uploaded successfully: {uploaded_file_name}")
        else:
            print(f"Test failed: {test_case} - Error: Uploaded file format is not valid: {uploaded_file_name}")

        # Wait a moment for the next test case
        driver.implicitly_wait(2)

finally:
    # Close the browser
    driver.quit()
