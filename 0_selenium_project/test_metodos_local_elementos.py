"""
MÉTODOS PARA LOCALIZAR ELEMENTOS

  - find_element(): retorna a primeira ocorrencia e erro se não encontrar
  - find_elements(): retorna todas as ocorrencias e não retorna erro se não encontrar
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as aguardar

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.saucedemo.com/v1/')

# find_element()
# username = browser.find_element(By.ID, "user-name")
# password = browser.find_element(By.ID, "password")

# send_keys
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")

# find_elements()
auth_fields = browser.find_elements(By.XPATH, "//input[@class='form_input']")

print(auth_fields)

print('->', len(auth_fields))
assert len(auth_fields) == 2, "O tamanho da lista de elementos, é diferente do esperado"

aguardar(5)

browser.quit()


