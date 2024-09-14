from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Ex. XAPTH irmão adjacente: //*[@id="topic"]/following-sibling::input
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://www.google.com')

# Mapear o container do iframe
iframe1 = browser.find_element(By.ID, 'frame1')

# Trocando para o iframe
browser.switch_to.frame(iframe1)

# Mapeando elementos dentro do iframe 1
browser.find_element(
    By.XPATH, '//*[@id="topic"]/following-sibling::input'
).send_keys('iframe1')
sleep(3)

# Trocando para o iframe dentro da iframe 1 que é iframe 3
iframe3 = browser.find_element(By.ID, 'frame3')
browser.switch_to.frame(iframe3)

# Mapeando elementos dentro do iframe 3 (Pq já estou dentro dele)
checkbox = browser.find_element(By.XPATH, '//[@type="checkbox"]')
checkbox.click()
sleep(3)

# Voltando (dois iframes para chegar na) para raiz da página
browser.switch_to.default_content()

# Mapeando outro iframe já na raiz da página
iframe2 = browser.find_element(By.ID, 'frame2')
browser.switch_to.frame(iframe2)

# Mapeando elementos dentro do iframe 2
dropdown = Select(browser.find_element(By.XPATH, '//select[@id="animals"]'))
dropdown.select_by_value("babycat")
sleep(3)