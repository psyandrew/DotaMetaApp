import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome() 

profile_dir = os.path.join('..','tmp','html','profiles')
mainpage_path = os.path.join('..', 'tmp', 'html', 'mainpage.html')
kda_path = os.path.join('..', 'tmp', 'html', 'kda_page.html') 
gpmxpm_path = os.path.join('..', 'tmp', 'html', 'gpmxpm_page.html') 



url = "https://www.dotabuff.com/heroes?show=heroes&view=economy&mode=all-pick&date=7d&rankTier=divine&position="
driver.get(url)

gpmxpm_page = driver.page_source
time.sleep(2)


#save the HTML content
with open(gpmxpm_path, "w", encoding="utf-8") as f:
    f.write(gpmxpm_page)

url = "https://www.dotabuff.com/heroes?show=heroes&view=winning&mode=all-pick&date=7d&rankTier=divine"
driver.get(url)

kda_page = driver.page_source
time.sleep(2)


#save the  HTML content
with open(kda_path, "w", encoding="utf-8") as f:
    f.write(kda_page)


#Load the webpage
url = "https://www.dotabuff.com/heroes?show=heroes&view=meta&mode=all-pick&date=7d&rankTier=divine"
driver.get(url)

# Get the mainpage HTML content
mainpage_file = driver.page_source
time.sleep(2)

#save the mainpage HTML content
with open(mainpage_path, "w", encoding="utf-8") as f:
    f.write(mainpage_file)

# Get table then Rows
table = driver.find_element(By.TAG_NAME, "tbody")
rows = table.find_elements(By.TAG_NAME, "tr")



#find <a>
for row in rows:

    link = row.find_element(By.CLASS_NAME, "tw-items-center")
    print('link found')
    href = link.get_attribute("href")
    print(href)

    driver.get(href)
    time.sleep(3)


    page_source = driver.page_source

    

    filename = driver.title + ".html"

    file_path = os.path.join(profile_dir, filename)


    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page_source)
        print(f"Saved HTML to {filename}")

    driver.back()
    time.sleep(3)

url = "https://www.dotabuff.com/heroes?show=heroes&view=economy&mode=all-pick&date=7d&rankTier=divine&position="
driver.get(url)

gpmxpm_page = driver.page_source

with open(mainpage_path, "w", encoding="utf-8") as f:
    f.write(gpmxpm_page)

url = "https://www.dotabuff.com/heroes?show=facets&view=winning&mode=all-pick&date=7d&rankTier=divine"
driver.get(url)

kda_page = driver.page_source

with open(mainpage_path, "w", encoding="utf-8") as f:
    f.write(kda_page)

driver.quit()


