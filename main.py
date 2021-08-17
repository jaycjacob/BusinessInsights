import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

driver = webdriver.Chrome("c:\\chromedriver.exe")

starting_bs = 'The carnivore restaurant'
country = 'kenya'
url = 'https://www.google.com/maps/search/' + starting_bs + ' ' + country

driver.get(url)

WebDriverWait(driver, 30)
time.sleep(30)
d = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/span[1]/span[1]/button')
d.click()
WebDriverWait(driver, 25)
time.sleep(30)
bs_names= [i.text for i in driver.find_elements_by_css_selector('[class="qBF1Pd gm2-subtitle-alt-1"]')]

ps = pd.DataFrame(data={'names':bs_names})
ps.to_csv('names.cvs', index = False)
print(bs_names)
driver.close()