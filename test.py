from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("http://127.0.0.1.5000")
    print (driver.title)
    
finally:
    driver.quit()