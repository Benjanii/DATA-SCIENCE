from selenium import webdriver

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'C:/Users/56997/Desktop/chrome-win64'

driver = webdriver.Chrome(path)
driver.get(website)

