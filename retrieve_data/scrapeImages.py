from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3
import argparse
import urllib.request
import pandas as pd
from time import sleep
import random

import scrape_config as sc
import requests
from shutil import copyfile

def query_confidence_values(image_path):
    fs = {"" : open(image_path, 'rb')}
    r = requests.post(sc.PIC_UPLOAD_URL, files=fs)
    json_data = json.loads(r.text)
    return (json_data["number_of_faces"], json_data["their_detection_scores"])

def download_gimags(search_term, max_count, dest_folder_path, chromedriver_path="C:\\Users\\heuzerjr\\chromedriver.exe"):
    # this function is based on code by github user: yeamusic21, from gist discussion:
    # https://gist.github.com/genekogan/ebd77196e4bf0705db51f86431099e57

    print("define program variables and open google images...")
    searchterm = search_term
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    browser = webdriver.Chrome(chromedriver_path)
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    counter = 0
    succounter = 0

    print("start scrolling to generate more images on the page...")
    # TODO scroll more if not sufficient face images are found
    for _ in range(500):
        browser.execute_script("window.scrollBy(0,10000)")

    # button_more_imgs = "/html/body/div[2]/c-wiz/div[4]/div[1]/div/div/div/div/div[5]/input"
    # browser.find_element_by_xpath(button_more_imgs).click()
    try:
        os.makedirs(dest_folder_path)
        one_face_folder_path = dest_folder_path + "oneFace\\"
        os.makedirs(one_face_folder_path)
        print("start scraping ...")

        # TODO: catch when not sufficient face images are found and scroll is over
        for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
            if succounter == max_count:
                break
            counter = counter + 1
            print("Total Count:", counter)
            print("Successful Count:", succounter)
            img = x.get_attribute('src')
            new_filename = "image"+str(counter)+".jpg"
            try:
                path = dest_folder_path
                path += new_filename
                urllib.request.urlretrieve(img, path)
                (n_faces, conf_vals) = query_confidence_values(path)
                if n_faces == 1 and conf_vals[0] >= sc.THRESHOLD_CONF_VALUE:
                    copyfile(path, one_face_folder_path + new_filename)
                    succounter += 1
            except Exception as e:
                print(e)
        print(succounter, "pictures succesfully downloaded")
        browser.close()
    except FileExistsError:
        print("skipping duplicate name " + search_term)

def csv_iterate(csv_path, n_imgs, save_path, max_sleep_time=5):
    csv_data = pd.read_csv(csv_path, header=None)

    # assuming there is no explicit index, just the position in the file
    names = csv_data.iloc[:,0]
    paths = []
    for n in names:
        print("working on name: " + n)
        search_term = n.replace(" ", "+")
        this_save_path = save_path + search_term + "\\"
        paths.append(this_save_path)
        download_gimags(search_term, n_imgs, this_save_path, sc.PATH_CHROMEDRIVER)
        sleep(random.random() * max_sleep_time)

    glossary = pd.DataFrame({
        'name' : names, 
        'picture_location' : paths
        })
    glossary.to_csv(save_path + "glossary.csv")

csv_iterate(sc.PATHS_MALE[0], sc.N_FACE_IMAGES_TO_SCRAPE, sc.PATHS_MALE[1])
csv_iterate(sc.PATHS_FEMALE[0], sc.N_FACE_IMAGES_TO_SCRAPE, sc.PATHS_FEMALE[1])
