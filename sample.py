from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browse =webdriver.Chrome("./chromedriver")
browse.get("https://www.google.com")
search_bar= browse.find_element_by_name("q")
print(search_bar)
search_bar.send_keys("gmail")
search_bar.send_keys(Keys.RETURN)
# driver.find_element_by_xpath("/html/body/div[7]/div/div[11]/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/a/div[1]/span").click()
# driver.find_element_by_name("email").send_keys("muthu@gmail.com")
# driver.find_element_by_name("password").send_keys("Muthu@2001")