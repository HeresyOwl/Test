#測試用無視窗Chrome讀取網頁並截圖 *******************************************
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://www.baidu.com')
driver.save_screenshot('C:/Users/浚銘/Desktop/test.png')
driver.quit()


#抓取台北自行車站資料 ******************************************************
# import requests
# import json
# import pymysql

# url = "http://data.taipei/youbike"
# data = requests.get(url).json()

# for key, value in data["retVal"].items():
  # sno = value["sno"]
  # sna = value["sna"]
  # print("NO.", sno, sna)

