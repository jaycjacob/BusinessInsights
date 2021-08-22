import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from tqdm import tqdm
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.touch_actions import TouchActions

driver = webdriver.Chrome("c:\\chromedriver.exe")

starting_bs = 'The carnivore restaurant'
country = 'kenya'
bs_names = []
#addresses = []
url = 'https://www.google.com/maps/search/' + starting_bs + ' ' + country

driver.get(url)

WebDriverWait(driver, 30)
time.sleep(30)
d = driver.find_element_by_xpath(
    '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/span[1]/span[1]/button')
d.click()
for i in tqdm(range(3), leave=False, desc='name scrapping round'):
 #   print(bs_names)
 #   print(adresses)
    time.sleep(30)

    for r in range(6):
        driver.execute_script("arguments[0].scrollIntoView();",
                              driver.find_elements_by_xpath('//div[@class="qBF1Pd gm2-subtitle-alt-1"]')[-1])
        time.sleep(5)
    #    touch_actions = TouchActions(driver)
    #    touch_actions.scroll_from_element(d[1],0,150).perform()
    #   time.sleep(15)

    bs = [i.text for i in driver.find_elements_by_css_selector('[class="qBF1Pd gm2-subtitle-alt-1"]')]
    ad = [i.text for i in driver.find_elements_by_css_selector('[class="ZY2y6b-RWgCYc"]')]

    bs_names += bs
#    adresses += ad

    try:
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='ppdPk-Ej1Yeb-LgbsSe-tJiF1e']"))).click()
    except ElementClickInterceptedException:
        break

ps = pd.DataFrame(data={'names': bs_names})
ps.to_csv('names.csv', index=False)
driver.close()
