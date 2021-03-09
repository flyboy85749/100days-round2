from selenium import webdriver

chrome_driver_path = "C:/Users/User1/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_titles = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "title": event_titles[n].text
    }

print(events)


driver.quit()
