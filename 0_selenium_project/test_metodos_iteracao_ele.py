"""
COMANDOS DE INTERAÇÃO COMELEMENTOS
  element.

  - click(): Clica em um elemento
  - send_keys(): Preenche campos de input
  - text: Pega o texto do elemento
  - get_attribute(): Pega o valor de um atributo do elemento
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://www.saucedemo.com/v1/')

username = browser.find_element(By.ID, 'user-name')
password = browser.find_element(By.ID, 'password')
button_submit = browser.find_element(By.ID, 'login-button')

# send_keys()
username.send_keys('standard_user')
password.send_keys('secret_sauce')
sleep(2)

# click()
button_submit.click()
sleep(2)

# text
products_title = browser.find_element(
    By.XPATH, '//div[@class="product_label" and text()="Products"]'
)
print(products_title.text)
assert products_title.text == 'Products'

# get_attribute()
# //img[@src and contains(@src, "backpack")]
# Ex. Xpath Prof:(//img[@class="inventory_item_img"])[1] indice

img = browser.find_element(
    By.XPATH, '(//img[@class="inventory_item_img"])[1]'
)

print(img.get_attribute('src'))
assert img.get_attribute('src') == 'https://www.saucedemo.com/v1/img/sauce-backpack-1200x1500.jpg'
