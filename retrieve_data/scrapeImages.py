from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3
import argparse
import urllib.request
import pdb
import pandas as pd
from time import sleep
import random

def download_gimags(search_term, max_count, dest_folder_path, chromedriver_path="C:\\Users\\heuzerjr\\chromedriver.exe"):
    # this function is based on code by github user: yeamusic21, from gist discussion:
    # https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

    print("define program variables and open google images...")
    searchterm = search_term
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    # NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
    browser = webdriver.Chrome(chromedriver_path)
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    counter = 0
    succounter = 0

    print("start scrolling to generate more images on the page...")
    # 500 time we scroll down by 10000 in order to generate more images on the website
    for _ in range(500):
        browser.execute_script("window.scrollBy(0,10000)")

    os.makedirs(dest_folder_path)
    print("start scraping ...")
    for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
        if succounter == max_count:
            break
        counter = counter + 1
        print("Total Count:", counter)
        print("Successful Count:", succounter)
        #print("URL:", x.get_attribute('src'))
        img = x.get_attribute('src')
        new_filename = "image"+str(counter)+".jpg"

        try:
            path = dest_folder_path
            path += new_filename
            urllib.request.urlretrieve(img, path)
            succounter += 1
        except Exception as e:
            print(e)

    print(succounter, "pictures succesfully downloaded")
    browser.close()


#csv_path = "XXXXX\\female_name_url.csv"
csv_path = "..\\..\\Scholar_data\\male_name_url_sample10.csv"
csv_data = pd.read_csv(csv_path, header=None)
names = csv_data.iloc[:,0]
for n in names:
    print("working on name: " + n)
    search_term = n.replace(" ", "+")
    download_gimags(search_term, 5, "..\\data\\male_sample10\\" + search_term + "\\")
    sleep(random.random() * 5)

#st = "Bill+Clinton"
#download_gimags(st, 10, "XXXX" + st + "\\")