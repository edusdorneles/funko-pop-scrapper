import json
from selenium import webdriver
from selenium.webdriver.common.by import By

funko_pop = []

driver = webdriver.Chrome()
driver.get("https://funko.com/on/demandware.store/Sites-FunkoUS-Site/en_US/Search-UpdateGrid?cgid=funko-fandoms&start=0&sz=5000")

products = driver.find_elements(By.CLASS_NAME, "product")

for product in products:
  product_info_container = product.find_element(By.CLASS_NAME, "tile-body")
  product_name = product_info_container.find_element(By.TAG_NAME, "a").text
  product_price = product_info_container.find_element(By.CLASS_NAME, "value").text
  product_image = product.find_element(By.CLASS_NAME, "tile-main-image").get_attribute("src")
  product_license = product_info_container.find_element(By.CLASS_NAME, "product-license").text

  funko_pop.append({
    "name": product_name,
    "price": product_price,
    "image": product_image,
    "license": product_license
  })

with open("funko_pop.json", "w") as json_file:
  json.dump(funko_pop, json_file, indent=2)
