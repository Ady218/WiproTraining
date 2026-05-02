"""
code for working with Google Homepage
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input('what browser do you wan to use?')

match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
    case _:
        print('Unknown browser - Not available. \n Executing with default EDGE browser.')
        #driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

#1st step
driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))      #(service=Service(EdgeChromiumDriverManager().install()))

driver.get("https://www.google.com")

pagetitle = driver.title



if pagetitle == 'Google':
    print("Google homepage loaded - Pass")
else:
    print("Google homepage loaded - Pass")

sleep(3) #not recommended

driver.quit
