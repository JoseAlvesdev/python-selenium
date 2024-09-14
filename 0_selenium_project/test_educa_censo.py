from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://censobasico.inep.gov.br/censobasico/#/')

def fazer_login():
    browser.find_element(By.ID, 'login').send_keys('07430909183')
    browser.find_element(By.ID, 'input_senha').send_keys('8972EA45Cd@')
    sleep(10) # resolver captcha manualmente
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    sleep(10)


fazer_login()