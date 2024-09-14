from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get('https://google.com.br')

sleep(10)
