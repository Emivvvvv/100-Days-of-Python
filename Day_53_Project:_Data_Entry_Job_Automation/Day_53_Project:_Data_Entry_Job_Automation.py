from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

chrome_driver_path = "/Users/emivvvvv/Development/chromedriver"

headers = {
    "User-Agent": "###",
    "Accept-Language": "###"
}

property_site_link = "###"
google_form_link = "###"

response = requests.get(url=property_site_link, headers=headers)
property_site_html = response.text
soup = BeautifulSoup(property_site_html, "html.parser")

addresses = soup.find_all(name="address", class_="list-card-addr")
addresses_list = [address.text for address in addresses]
prices = soup.find_all(name="div", class_="list-card-price")
prices_list = [price.text for price in prices]
links = soup.find_all(name="a", class_="list-card-link list-card-link-top-margin")
links_list = []
for link in links:
    href = link["href"]
    print(href)
    if "http" not in href:
        links_list.append(f"###{href}")
    else:
        links_list.append(href)

driver = webdriver.Chrome(chrome_driver_path)
for i in range(0, len(prices_list)):
    driver.get(google_form_link)
    address_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    time.sleep(2)
    address_box.send_keys(addresses_list[i])
    price_box.send_keys(prices_list[i])
    link_box.send_keys(links_list[i])
    submit_button.click()


