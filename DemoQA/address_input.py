import time
from selenium.webdriver.common.by import By


def address_input_field_validation(driver):
    try:
        address = "ka 32 Nasrin Mintu Road, Nadda, Dhaka -1212"
        driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(address)
        time.sleep(2)
    except Exception as e:
        print('Handle exception: ', e)
