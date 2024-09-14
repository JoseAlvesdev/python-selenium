from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Novos Imports
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://josealvesdev.github.io/calcular-frequencia/')

# Selecionar por texto visível
# dropdown_products = Select(browser.find_element(By.CLASS_NAME, 'c-select-month'))
# dropdown_products.select_by_visible_text('Agosto')
# sleep(5)

# Selecionar por valor do atributo value="value"
# dropdown_products = Select(browser.find_element(By.CLASS_NAME, 'c-select-month'))
# dropdown_products.select_by_value('agosto')
# sleep(5)

# Selecionar por index
# dropdown_products = Select(browser.find_element(By.CLASS_NAME, 'c-select-month'))
# dropdown_products.select_by_index(7)
# sleep(5)

# Selecionar multiplos valores OBS PEGAR XPATH do container
# dropdown_products = Select(browser.find_element(By.CLASS_NAME, 'c-select-month'))
# dropdown_products.select_by_visible_text('Agosto')
# dropdown_products.select_by_visible_text('Outubro')
# dropdown_products.select_by_visible_text('Dezembro')
# sleep(5)
