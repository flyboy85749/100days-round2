from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/User1/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_total = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]')
# article_total.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()


search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
