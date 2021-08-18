import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from tqdm import tqdm
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome("c:\\chromedriver.exe")

starting_bs = 'The carnivore restaurant'
country = 'kenya'
bs_names = []
url = 'https://www.google.com/maps/search/' + starting_bs + ' ' + country

driver.get(url)

WebDriverWait(driver, 30)
time.sleep(30)
d = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/span[1]/span[1]/button')
d.click()
for i in tqdm(range(3), leave = False, desc = '1. 1st round'):
    print(bs_names)
    time.sleep(30)
    WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.CLASS_NAME, "section-layout siAUzd-neVct-Q3DXx-horizontal")))
    
    bs= [i.text for i in driver.find_elements_by_css_selector('[class="qBF1Pd gm2-subtitle-alt-1"]')]
    bs_names = bs

    try:
        WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ppdPk-Ej1Yeb-LgbsSe-tJiF1e']"))).click()
    except ElementClickInterceptedException:
        break

ps = pd.DataFrame(data={'names':bs_names})
ps.to_csv('names.csv', index=False)
print(bs_names)
driver.close()