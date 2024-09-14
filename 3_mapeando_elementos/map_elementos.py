"""
MAPEAMENTO DE ELEMENTOS

  Elemento html: <input class="c-form__input" /> ou seja:
    <input class="c-form__input" />
    <input [attribute]=["value" ]/>

  Locators

    Comuns
      São mais diretos

      1 - ID
      2 - NAME
      3 - LINK_TEXT: <a href="...">
      4 - PARTIAL_LINK_TEXT: <a href="..."> link parcial trecho do link
      5 - CLASS_NAME
      6 - TAG_NAME

    Customizáveis

      1 - CSS_SELECTOR
        - TAG AND ID
        - TAG AND CLASS
        - TAG AND ATTRIBUTE
        - TAG, CLASS AND ATTRIBUTE
        - InnerText

      2 - XPATH (mais utilizado) id || XPATH

    Usando locators
      Chamando o metodo find_element(Class.locator, element.locator.value)

      1 - By.ID
        browser.find_element(By.ID, "password")

      2 - By.NAME
        browser.find_element(By.NAME, "password")

      3 - By.LINK_TEXT
        element: <a href="...">Twitter</a>
        element: <a href="...">[LINK_TEXT]</a>

        browser.find_element(By.LINK_TEXT, "Twitter")


      4 - By.PARTIAL_LINK_TEXT
        element: <a href="...">|Twi|tter</a>
        element: <a href="...">[PARTIAL_LINK_TEXT]</a>

        browser.find_element(By.PARTIAL_LINK_TEXT, "Twi")


      5 - By.CLASS_NAME
        browser.find_element(By.CLASS_NAME, "c-form__input")
          Retorna primeira ocorrência

        OBS.: Para retornar todas as ocorrências muda o método
        browser.find_elements(By.CLASS_NAME, "c-form__input")
          Retorna todas as ocorrências

        OBS.: find_element() se nenhuma ocorrencia for encontrada retorna erro,
        find_elements() se nenhuma ocorrencia for encontrada não retorna erro,
        retorna 0.


      6 - By.TAG_NAME
        <input class="c-form__input" />
        <[TAG_NAME] class="c-form__input" />

        browser.find_element(By.TAG_NAME, "c-form__input")
          Retorna primeira ocorrência

        OBS.: Para retornar todas as ocorrências muda o método
        browser.find_elements(By.TAG_NAME, "c-form__input")
          Retorna todas as ocorrências

        OBS.: find_element() se nenhuma ocorrencia for encontrada retorna erro,
        find_elements() se nenhuma ocorrencia for encontrada não retorna erro,
        retorna 0.

        
      7 - By.CSS_SELECTOR
        browser.find_element(By.CSS_SELECTOR, "input#c-form__input")

        - tag_name#id_value (tag é opcional)
          browser.find_element(By.CSS_SELECTOR, "#c-form__input")

        - tag_name.class_value (tag é opcional)
          browser.find_element(By.CSS_SELECTOR, "input.c-form__input")

        - tag_name[attibute=value] (tag é opcional)
          browser.find_element(By.CSS_SELECTOR, "[type=password]")

        Combinação de seletores
        - tag_name.class_name[attibute=value] (tag é opcional)
          browser.find_element(By.CSS_SELECTOR, ".c-form__input[type=password]")


      8 - XPath

        XPath é uma sintaxe para definir partes de um documento XML
        XPath pode ser usado para navegar por elementos e atributos em um documento XML
        XPath usa expressões de caminho para navegar em documentos XML
        XPath contém uma biblioteca de funções padrão
        XPath é usado para localizar elementos em uma página web por meio do DOM
        XPath é o endereço do elemento em uma página

        link: https://www.w3schools.com/xml/xpath_intro.asp

        XPath

          Absolute/Full XPath
          Relative/Partial XPath

          FULL
          /html/body/div[5]/ui-view/form/div/div[5]/button


          PARTIAL (recomendado pelo professor)
          //*[@id="login-box"]/div[5]/button

        Funções
          - contains()
          - text()
          - and / or
          - |
          - =

        Construindo XPaths

          Ex.1: //select[@class="product_sort_container"]
          Ex.2: //div[@id="shopping_cart_container"]/a[@class="shopping_cart_link"]
          Ex.3: //div[contains(text(), "Get your testing superhero on with the Sauce Labs")]

          * contains() == contem()
          Ex.4: //*[contains(@class, "inventory")]

          * text() == texto() e and == e
          Ex.5: //*[contains(@class, "inventory") and contains(text(), "Get your testing superhero on with the Sauce Labs")]
          
          * or == ou
          Ex.6: //*[contains(@class, "inventory") or contains(text(), "Get your testing superhero on with the Sauce Labs")]

          * | == ou e = igual ==
          Ex.7: //div[@class="inventory_item_price" and contains(text(), "29.99")] | //div[@class="inventory_item_price" and text()="9.99"]

          atende um XPath ou outro XPath (no meio de XPaths)

    OBS.: É possível ativar um search no devtools CTRL + F
      
"""
