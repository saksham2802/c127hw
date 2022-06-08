from bs4 import BeautifulSoup
from selenium import webdriver 
import time 
import csv 
start_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(start_url)
time.sleep(10)
def scrap():
    headers=["Name","Light_Years_from_Earth","Planet_Mass","Stellar Magnitude","Discovery Date"]
    planetdata=[]
    for i in range(0,202):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags= ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                     try:
                         temp_list.append(li_tag.contents[0])
                     except:
                         temp_list.append("")
            planetdata.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)
scrap()
