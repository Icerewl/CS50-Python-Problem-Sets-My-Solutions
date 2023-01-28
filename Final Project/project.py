from typing import Type
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import urllib.request
import pathlib
import os
import glob
import sys
from account_info import mail,mail_password


driver = webdriver.Firefox()
driver.set_window_size(1920,1080)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
img_urls_list = []
title_list = []
url_list = []
current_directory = pathlib.Path(__file__).parent.resolve()

def main():
    try:
        if sys.argv[2]:
            pass
    except:
        print("Usage: project.py --product --how many products to be posted")
        raise TypeError
    
    if type(sys.argv[1]) != type("string"):
        raise TypeError("Only text is allowed")
    
    
    sys.argv[-1] = int(sys.argv[-1])
    if len(sys.argv) > 3:
       name_of_products  = sys.argv[-3] + " " + sys.argv[-2]
       
    else:
        name_of_products = sys.argv[1]
    if sys.argv[-1] < 1 or sys.argv[-1] > 100:
        raise TypeError("Product number must be between 1 and 100")
    aliexpress(name_of_products,sys.argv[-1])

    login_website(mail,mail_password)

    create_a_post(sys.argv[2])
def login_website(login_id,login_password):
    if type(login_id) == type("s") and type(login_password) == type("s"):
        #while True:
            driver.get("https://tr.pinterest.com/")
            login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div'))).click()
            email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
            password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
            email.send_keys(login_id)
            time.sleep(1)
            password.send_keys(login_password)
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div/div/div/div/div[4]/form/div[7]/button').click()
            time.sleep(3/2)
            """
            if driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div/div/span'):
                print("Successfuly Logged in")
                break
            """
            print("Something went wrong. Still trying to log in")
    else:
        print("Failed to log in.Login info cannot be integers")

def create_a_post(product_count):
    try:
        counter = 0
        for i in range(product_count):
            if counter >= product_count:
                break
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div/div/span'))).click()
            create_post_click = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div/a/div/div[1]/div/div/span'))).click()
            description_area = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/textarea')))
            description_area.send_keys(url_list[counter])
            time.sleep(1)
            title_area = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div[1]/textarea')
            title_area.send_keys(title_list[counter][0:98])
            time.sleep(1)
            upload = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/input')
            upload.send_keys(str(current_directory) + r"\images\image{}.png".format(counter))
            time.sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]'))).click()
            time.sleep(5)
            driver.get('https://tr.pinterest.com/')
            counter += 1
        #For deleting all images
        files = glob.glob(str(current_directory) + r"\images\*")
        for f in files:
            os.remove(f)
        return True
    

    except:
        print("Something went wrong. Couldn't Create the post.")
        driver.get('https://tr.pinterest.com/')
        return False

def aliexpress(search_sentence,product_count):
    
    driver.get('https://www.aliexpress.com/')
    
    p = driver.current_window_handle
    try :        
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div[1]/img[2]'))).click()
    except:
        pass  
    driver.find_element(By.XPATH, '//*[@id="search-key"]').send_keys(search_sentence)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/form/div[1]/input'))).click()
    
    counter = 1
    for i in range(product_count):
        #wait.until(EC.element_to_be_clickable((By.TAG_NAME,'html'))).send_keys(Keys.END)
        time.sleep(2)
        if counter > product_count:
            break
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a._3t7zg:nth-child({counter}) > div:nth-child(1) > img:nth-child(1)'))).click()
        
        driver.switch_to.window(driver.window_handles[1])
        idk = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).get_attribute("innerHTML")
        title_list.append(idk)
        src = driver.find_elements(By.TAG_NAME, "img")
        src = src[counter].get_attribute("src")
        src = src.replace("50x50","Q90")
        img_urls_list.append(src)
        url_list.append(driver.current_url)
        time.sleep(1)
        counter += 1
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    
    counter_for_image = 0
    for i in range(len(img_urls_list)):
        if counter_for_image >= len(img_urls_list):
            break
        
        a = str(current_directory) + r"\images\image{}.png".format(counter_for_image)
        urllib.request.urlretrieve(img_urls_list[counter_for_image],a)
        driver.get(img_urls_list[counter_for_image])
        counter_for_image += 1
    return True

    
    
if __name__ == "__main__":
    main()

    
