"""
CONFIGURANDO O SELENIUM
  1 - Entrar na documentação oficial 
    link: https://www.selenium.dev/

    menu > dowloads > Python > Versao Estável 
    > Copiar o comando do terminal de instalaçaõ :/ > ATIVAR AMBIENTE VIRTUAL
    > Executar: pip install selenium

    comando pra verificar instalação: pip show selenium

    1 - importar o modulo do selenium
      
      from selenium import webdriver

    2 - Criar um objeto/instância da classe Chrome()

      browser = webdriver.Chrome()

    3 - Usar o método get(1parâ -> url) para abrir o navegador

      browser.get()

    DICA: Boas práticas de testes com Python, nomear arquivos com um prefixo,
    de test_ (na frente).

    IMPORTANTE: Não mudar o nome da pasta após o ambiente estiver pronto.

    OBS.: Estudar biblioteca time
"""