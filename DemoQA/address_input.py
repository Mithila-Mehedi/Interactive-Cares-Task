from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_driver_path = "H:\Interactive-Cares-Task\chromedriver.exe"

# Set ChromeDriver path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

address = "ka 32 Nasrin Mintu Road, Nadda, Dhaka -1212"

# Open the website
driver.get("https://demoqa.com/automation-practice-form")

current_address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(address)
time.sleep(2)
print("Pass: Sucessfully added the address")

driver.quit()
