from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/User1/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://still-eyrie-18622.herokuapp.com/")

first_input = driver.find_element_by_name("firstName")
first_input.send_keys("William")
last_input = driver.find_element_by_name("lastName")
last_input.send_keys("Hall")
email_input = driver.find_element_by_name("email")
email_input.send_keys("billhall168@gmail.com")
button = driver.find_element_by_tag_name("button")
button.click()
