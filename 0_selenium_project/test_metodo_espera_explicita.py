import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Importes necessários para espera explícita
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('http://127.0.0.1:5500/index.html')

# Colocar um intervalo máximo do evento acontecer
wait = WebDriverWait(browser, 30)

# Alert is present | until == ate
browser.find_element(
    By.XPATH, '//button[contains(text(), "uma alet") and @class]'
).click()
wait.until(EC.alert_is_present())

"""
Ex.2
text_to_be_present_in_element
browser.find_element(By.ID, "populate-text").click()
wait.until(EC.text_to_be_present_in_element(
    By.XPATH, '//*[@class="target-text"]'), "Selenium Webdriver"
)
assert target_text == "Selenium Webdriver"

Ex.3
element_to_be_clickable
browser.find_element(By.ID, "display-other-button").click()
wait.until(EC.element_to_be_clickable((By.ID, 'hidden')))

Ex.4
element_to_be_clickable
browser.find_element(By.ID, "display-other-button").click()
wait.until(EC.element_to_be_clickable((By.ID, 'disable')))

Ex.:
element_to_be_selected
checkbox = browser.find_element(By.ID, 'ch')
browser.find_element(By.ID, 'checkbox').click()
wait.until(EC.element_to_be_selected(checkbox))

"""
