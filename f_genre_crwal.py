import selenium
from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import csv
import warnings
from selenium.webdriver.common.keys import Keys
warnings.filterwarnings(action='ignore')
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver
def ts(n):
    time.sleep(n)
def xp(n):
    driver.find_element_by_xpath(n).click()
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
webdriver.ChromeOptions().add_experimental_option("excludeSwitches",["enable-logging"])
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
driver.maximize_window()
url = 'https://www.melon.com/search/song/index.htm?q=.&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&mwkLogType=T'
ts(1)
f=open("C:/Users/PC/Desktop/BDPFINALanalysis.csv",'r',encoding="utf-8")
r=csv.reader(f)
r=list(map(list,zip(*r)))
for song in r[0]:
    driver.get(url)
    driver.find_element_by_css_selector("#top_search.ui-autocomplete-input").clear()
    driver.find_element_by_css_selector("#top_search.ui-autocomplete-input").send_keys(song)
    driver.find_element_by_css_selector("#top_search.ui-autocomplete-input").send_keys(Keys.ENTER)
    ts(0.2)
    driver.find_element_by_xpath('//*[@id="frm_defaultList"]/div/table/tbody/tr/td[3]/div/div/a[1]/span').click()
    ts(0.2)
    gen=driver.find_elements_by_css_selector("#downloadfrm > div > div > div.entry > div.meta > dl > dd:nth-child(6)")
    sg=[song,gen[0].text]
    with open("C:/Users/PC/Desktop/BDPFINALanalyfinal.csv","a",encoding='utf-8-sig',newline='') as f:
                    writer=csv.writer(f)
                    writer.writerow(sg)
                    f.close()
'''
dataframe=pd.DataFrame(r)
dataframe.to_csv("C:/Users/PC/Desktop/BDPFINALanalyfinal.csv",header=False,index=False,encoding='utf-8-sig')
                wr.append(week_data)
'''
'''
dataframe=pd.DataFrame(wr)
dataframe.to_csv("C:/Users/PC/Desktop/BDPFINAL.csv",header=False,index=False,encoding='utf-8-sig')
'''
