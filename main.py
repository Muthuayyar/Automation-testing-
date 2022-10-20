from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
s = Service("C:/Users/ASM/Desktop/Automation testing/chromedriver")
browse =webdriver.Chrome(service=s)
browse.get("https://www.google.com")
search_bar= browse.find_element(By.NAME,"q")
search_bar.send_keys("LinkedIn")
search_bar.send_keys(Keys.RETURN)
browse.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3").click()
browse.find_element(By.NAME,"session_key").send_keys("muthuthangam1604@gmail.com")
browse.find_element(By.NAME,"session_password").send_keys("Muthu@19")
browse.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
#browse.find_element(By.NAME,"phoneNumber").send_keys("6385585783")
#browse.find_element(By.NAME,"pin").send_keys("993530")
#browse.find_element(By.XPATH,"/html/body/div/main/form/div[2]/button").click()
#browse.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div/a/div[1]/img").click()












