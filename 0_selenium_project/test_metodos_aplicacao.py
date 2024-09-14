"""
METODO DA APLICAÇÃO
  
  - title: Titulo
  - current_url: Url
  - page_source: Código fonte

"""

import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/v1/')

print('->', browser.title)
print('->', browser.current_url)
print('->', browser.page_source)
