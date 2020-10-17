#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver

browser = webdriver.Chrome('D:\chromedriver.exe')

#This is the main line 
browser.maximize_window()
browser.get('https://google.com')


# In[ ]:




