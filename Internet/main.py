from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path_to_chromedriver = "C:\python_practice\chromedriver-win64\chromedriver.exe"

service = Service(path_to_chromedriver)
driver = webdriver.Chrome(service=service)

driver.get("https://www.example.com")

driver.execute_script("localStorage.setItem('key', 'value');")

value = driver.execute_script("return localStorage.getItem('key');")
print(value)

driver.execute_script("localStorage.removeItem('key');")

driver.refresh()

driver.add_cookie({"name": "key", "value": "myVal"})

cookies = driver.get_cookies()
for cookie in cookies:
    if cookie['name'] == 'key':
        value = cookie['value']
        print(value)

driver.delete_cookie("key")

driver.quit()