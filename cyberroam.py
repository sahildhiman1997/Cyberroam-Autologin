from selenium import webdriver
import time
import pyautogui

chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get('http://172.20.20.1:8090') 			  #change the address to your desired address.
time.sleep(5)

username=browser.find_element_by_name('username')
username.send_keys("test")                 			 #change username here
password=browser.find_element_by_name('password')
password.send_keys("test")              			 #change password here      
pyautogui.hotkey("Enter")
pyautogui.hotkey("Ctrl","w")