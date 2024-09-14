"""
PROBLEMAS DE IMCOMPATIBILIDADE COM O DRIVER
  1 - Instalar o Selenium webdriver manager

  from selenium.webdriver.chrome.service import Service as ChromeService
  from webdriver_manager.chrome import ChromeDriverManager

  browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())

ATUALIZANDO A VERSÃO ATUAL DO SELENIUM
  Atualizando o pacote no nosso ambiente

  pip install webdriver-manager -u
"""