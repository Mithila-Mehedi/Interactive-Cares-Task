import logging
import time

from selenium.webdriver.common.by import By

from selenium import webdriver
from email_input import email_input_field_validation
from name_input import name_input_field_validation
from gender_input import gender_input_field_validation
from mobile_input import mobile_input_field_validation
from dob_input import dob_input_field_validation
from hobbies_input import hobbies_input_field_validation
from picture_input import picture_input_field_validation
from address_input import address_input_field_validation
from state_and_city import state_input_field_validation
from subjects_input import subject_input_field_validation


# import test data
from testdata.data import test_emails, test_names, test_genders, test_mobiles, test_dates, test_pictures, test_states, test_subjects

DEMOQA_URL = 'https://demoqa.com/automation-practice-form'

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='logger.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')


# Set ChromeDriver path
driver = webdriver.Chrome()

# Open the website
driver.get(DEMOQA_URL)


def main():
    try:
        logging.debug('Starting the automation test!!')
        name_input_field_validation(driver, test_names)
        email_input_field_validation(driver, test_emails)
        gender_input_field_validation(driver, test_genders)
        mobile_input_field_validation(driver, test_mobiles)
        dob_input_field_validation(driver, test_dates)
        subject_input_field_validation(driver, test_subjects)
        hobbies_input_field_validation(driver)
        picture_input_field_validation(driver, test_pictures)
        address_input_field_validation(driver)
        state_input_field_validation(driver, test_states)
        driver.find_element(By.XPATH, "//button[@id='submit']").click()
        time.sleep(9)
    finally:
        logging.debug('Automation script run successful!!')
        driver.quit()


if __name__ == '__main__':
    main()
