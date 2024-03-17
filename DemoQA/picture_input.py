import os
import time
from selenium.webdriver.common.by import By


def picture_input_field_validation(driver, picture_inputs):
    valid_file_formats = ["png", "jpeg", "jpg"]
    try:
        for idx, (test_case, file_path) in enumerate(picture_inputs):
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

            if file_extension in valid_file_formats:
                print(f"Test passed: {test_case} - File uploaded successfully: {uploaded_file_name}")
            else:
                print(f"Test failed: {test_case} - Error: Uploaded file format is not valid: {uploaded_file_name}")

            # Wait a moment for the next test case
            driver.implicitly_wait(2)

    except Exception as e:
        print('Handle error: ', e)
