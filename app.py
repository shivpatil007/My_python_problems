from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import playsound

driver = webdriver.Chrome()
driver.get("https://selfregistration.cowin.gov.in/")
phone = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
phone.send_keys('Add your no.')
phone_button = driver.find_element_by_css_selector(
    '#main-content > app-login > ion-content > div > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(1) > ion-grid > form > ion-row > ion-col.col-padding.md.hydrated > div > ion-button')
phone_button.click()
time.sleep(30)
otp_button = driver.find_element_by_css_selector(
    '#main-content > app-login > ion-content > div > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col > ion-grid > form > ion-row > ion-col:nth-child(3) > div > ion-button')
otp_button.click()
time.sleep(5)
shedul = driver.find_element_by_css_selector(
    '#main-content > app-beneficiary-dashboard > ion-content > div > div > ion-grid > ion-row > ion-col > ion-grid.beneficiary-box.md.hydrated > ion-row.sepreetor.ng-star-inserted.md.hydrated > ion-col > ion-grid > ion-row.dose-data.md.hydrated > ion-col:nth-child(2) > ul > li > a')
shedul.click()
time.sleep(1)
shedul_now = driver.find_element_by_css_selector(
    '#main-content > app-beneficiary-dashboard > ion-content > div > div > ion-grid > ion-row > ion-col > ion-grid.beneficiary-box.md.hydrated > ion-row:nth-child(4) > ion-col > div > div:nth-child(2) > div > ion-button')
shedul_now.click()
time.sleep(10)
search = driver.find_element_by_css_selector(
    '#main-content > app-appointment-table > ion-content > div > div > ion-grid > ion-row > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(2) > form > ion-grid > ion-row > ion-col.col-padding.ion-text-start.ng-star-inserted.md.hydrated > ion-button')
search.click()
time.sleep(1)
etinpls = driver.find_element_by_xpath(
    '/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[5]/div/div[2]/input')
etinpls.click()
time.sleep(5)
for i in range(6):
    search.send_keys(Keys.ARROW_DOWN)

a = 'NA'
b = 'NA'
c = 'NA'
d = 'NA'

while(a == 'NA' and b == 'NA' and c == 'NA' and d == 'NA'):
    for i in range(15):
        search.send_keys(Keys.ARROW_DOWN)
    tp1 = driver.find_elements_by_xpath(
        '/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[8]/div/div/mat-selection-list/div[1]/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li[2]/div/div/a')
    tp2 = driver.find_elements_by_xpath(
        '/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[8]/div/div/mat-selection-list/div[2]/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li[2]/div/div/a')
    tp3 = driver.find_elements_by_xpath(
        '/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[8]/div/div/mat-selection-list/div[3]/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li[2]/div/div/a')
    tp4 = driver.find_elements_by_xpath(
        '/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[8]/div/div/mat-selection-list/div[4]/mat-list-option/div/div[2]/ion-row/ion-col[2]/ul/li[2]/div/div/a')

    a = tp1[0].text
    b = tp2[0].text
    c = tp3[0].text
    d = tp4[0].text

    for i in range(15):
        search.send_keys(Keys.ARROW_UP)
    search.click()
    time.sleep(3)

playsound.playsound('01 - Blue Eyes - DownloadMing.SE.mp3', True)
