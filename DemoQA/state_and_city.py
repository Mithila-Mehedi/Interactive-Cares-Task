import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def state_input_field_validation(driver, test_states):
    try:
        for state, cities in test_states.items():
            time.sleep(2)
            driver.find_element(By.XPATH, "//div[@id='state']").click()
            time.sleep(1)
            state_input = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
            state_input.send_keys(state)
            time.sleep(1)
            state_input.send_keys(Keys.ENTER)
            time.sleep(2)

            for city in cities:
                driver.find_element(By.XPATH, "//div[@id='city']").click()
                time.sleep(1)
                city_input = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
                city_input.send_keys(city)
                time.sleep(1)
                city_input.send_keys(Keys.ENTER)

                print(f'City and state selected. State: {state}, city: {city}')
                time.sleep(1)
    except Exception as e:
        print('Handle exception: ', e)

