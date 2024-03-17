import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def subject_input_field_validation(driver, test_subjects):
    try:
        for idx, subject in enumerate(test_subjects):
            subjects = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
            subjects.send_keys(subject)
            subjects.send_keys(Keys.ENTER)
            time.sleep(2)
            print(f"Successfully enter {subject} from auto suggestions")

        driver.find_element(By.XPATH, "(//*[name()='svg'][@class='css-19bqh2r'])[2]").click()
        time.sleep(2)
        print("subjects removed successfully")
    except Exception as e:
        print('Handle exception: ', e)
