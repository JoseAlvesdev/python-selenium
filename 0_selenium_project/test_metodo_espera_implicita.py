"""
COMANDOS DE ESPERA (WAIT)
  element.

  - time.sleep()
  - implicitly_wait: 
  - explicitly_wait: 

  OBS.: Usar sleep() só em ultimo caso.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

# A qulquer comando esperar até 12 segundos
# browser.implicitly_wait(12)


browser.maximize_window()
browser.get('http://127.0.0.1:5500/index.html')

checkbox = browser.find_element(By.XPATH, '//input[@type="checkbox"]')
assert checkbox.is_displayed()
sleep(3)
print('Checkbox está na tela!')
print(checkbox)