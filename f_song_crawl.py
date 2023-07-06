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
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
ts(1)
wr=[]
driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[4]/a/span').click()
driver.find_element_by_xpath('//*[@id="conts"]/div[3]/div/button').click()
driver.find_element_by_xpath('//*[@id="conts"]/div[3]/div/div/dl/dd[2]/a').click()
driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[1]').click()
ts(1)
#era 1~5
for i in range(4,6):
    try:
        driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li['+str(i)+']/span/label').click()
        ts(0.5)
    except:
        continue
    for j in range(1,11):
#year 1~10
        try:
            driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li['+str(j)+']/span/label').click()
            ts(0.5)
        except:
            continue
        rank_y=driver.find_elements_by_css_selector("#d_chart_search > div > div > div.box_chic.nth2.view.on > div.list_value > ul > li:nth-child("+str(j)+") > span > label")
        for k in range(12,0,-1):
            try:
#month 12~1
                driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li['+str(k)+']/span/label').click()
                ts(0.5)
            except:
                continue
            for l in range(6,0,-1):
#week 6~1 
                try:
                    driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[4]/div[1]/ul/li['+str(l)+']/span/label').click()
                    ts(0.5)
                except:
                    continue
#genre all
                driver.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[1]/span/label').click()
                ts(0.5)
                xp('//*[@id="d_srch_form"]/div[2]/button/span/span')
                ts(1)
                rank01=driver.find_elements_by_css_selector("#lst50 > td:nth-child(4) > div > div > div.ellipsis.rank01 > span > strong > a")
                rank_d=driver.find_elements_by_css_selector("#d_chart_search > div > div > div.box_chic.nth4.view.on > div.list_value > ul > li:nth-child("+str(l)+") > span > label")
                week_data=[rank_y[0].text,rank_d[0].text,rank01[0].text]
                with open("C:/Users/PC/Desktop/BDPFINAL0.csv","a",encoding='utf-8-sig',newline='') as f:
                    writer=csv.writer(f)
                    writer.writerow(week_data)
                    f.close()
'''
                wr.append(week_data)
'''
'''
dataframe=pd.DataFrame(wr)
dataframe.to_csv("C:/Users/PC/Desktop/BDPFINAL.csv",header=False,index=False,encoding='utf-8-sig')
'''
