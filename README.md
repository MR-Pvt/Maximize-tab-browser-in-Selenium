# Maximize-tab-browser-in-Selenium

### for this you will need 
1. Selenium
2.  WebDriver


### And you have to import this

from selenium import webdriver



### Then you have to put the driver in a Directory and put the path in this line of code (It does not matter if you have opera of firefox driver just put in the path and this will work)

browser = webdriver.Chrome('D:\chromedriver.exe')



### Then For Maximizing the window of browser use this

browser.maximize_window()


### Here put in the address you like to open after https://
browser.get('https://google.com')


### The whole code is in ( .py ) file
