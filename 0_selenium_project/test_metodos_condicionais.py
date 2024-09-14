"""
MÉTODOS CONDICIONAIS 
  element.

  - is_displayed(): Diz se o elemento está sendo mostrado na tela ou não
  - is_enabled(): Diz se o elemento está habilitado ou não
  - is_selected(): Diz se o elemento está selecionado ou não

  assert espera true ou falso

  Retorna True ou False
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://demo.applitools.com/')

username = browser.find_element(By.ID, 'username')
check_remember_me = browser.find_element(
    By.XPATH, '//input[@type="checkbox" and contains(@class, "check")]'
)

# is_displayed()
print('Diplayed')
print('user: ', username.is_displayed())
print('check: ', check_remember_me.is_displayed())
assert username.is_displayed()
assert check_remember_me.is_displayed()

# is_enabled()
print('\n', 'Enabled')
print('user: ', username.is_enabled())
print('check: ', check_remember_me.is_enabled())
assert username.is_enabled()
assert check_remember_me.is_enabled()

# is_selected()
print('\n', 'Selected')
print('check: ', check_remember_me.is_selected())
assert not check_remember_me.is_selected()


# Clicando no checkbox
check_remember_me.click()
sleep(2)
print('check: ', check_remember_me.is_selected())
assert check_remember_me.is_selected()

