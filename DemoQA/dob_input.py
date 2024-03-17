import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import logging

# Initialize WebDriver
chrome_driver_path = "H:\Interactive-Cares-Task\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the website
driver.get("https://demoqa.com/automation-practice-form")

date_test_inputs = [
    ("past_date", "1998-July-17"),
    ("future_date", "2025-December-31")
]

try:
    for idx, (date_state, date) in enumerate(date_test_inputs):
        print(f"### Running date test case {idx + 1} with input {date} ###")

        # Find the date of birth input field
        dob_input = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
        dob_input.click()

        # Extract year, month, and day from the past date
        year, month, day = date.split("-")

        # Find the year and month dropdowns in the calendar dropdown
        year_select = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']"))
        month_select = Select(driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']"))

        # Select the past year and month
        year_select.select_by_visible_text(year)
        time.sleep(2)  # Wait for the calendar to update
        month_select.select_by_visible_text(month)
        time.sleep(2)  # Wait for the calendar to update


        # Find and select the past day
        date_element = driver.find_element(By.XPATH, f"//div[contains(text(),'{day}')]")
        date_element.click()

        # Wait for the calendar to close
        time.sleep(2)

        # Validate the selected date
        selected_date = dob_input.get_attribute("value")
        date_obj = datetime.strptime(selected_date, "%d %b %Y")
        formatted_date = date_obj.strftime("%Y-%B-%d")

        if date_state == 'future_date' and formatted_date == date:
            print('Error: Future date should not be selected')
        elif date_state == 'past_date' and formatted_date == date:
            print('Success: Date is selected correctly')
        else:
            print('Error: Selected date does not match the expected date')
finally:
    # Close the browser
    driver.quit()
