from selenium import webdriver
import time

driver=webdriver.Firefox()

driver.maximize_window()

url="https://www.google.com"

driver.get(url)

print(driver.title)
print(driver.current_url)

driver.save_screenshot('google.png')

print("Screenshot Taken")



driver.quit()
time.sleep(10)