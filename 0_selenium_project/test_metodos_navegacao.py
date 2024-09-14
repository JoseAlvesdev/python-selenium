"""
Metodos de navegação
  - get(): abre uma url
  - maximize_window(): Maximiza a tela
  - refresh(): atualiza página
  - back(): volta uma página
  - forward(): avança uma página
  - close(): fecha uma guia (separador)
  - quit(): mata o processo e fecha tudo
"""

import time
from selenium import webdriver

browser = webdriver.Chrome()

# maximize_window()
browser.maximize_window()
# browser.manimize_window()

# get()
browser.get('https://google.com.br')

# refresh()
time.sleep(2)
browser.refresh()
time.sleep(2)

# back()
browser.get('https://www.saucedemo.com/v1/')
time.sleep(2)
browser.back()

# forward()
time.sleep(2)
browser.forward()

# Abrindo nova guia
browser.switch_to.new_window("tab")
time.sleep(2)

# # close()
# browser.close()
# time.sleep(2)

# quit()
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(3)
browser.quit()
