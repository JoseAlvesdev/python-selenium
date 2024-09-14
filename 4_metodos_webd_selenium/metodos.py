"""
Métodos de navegação
Métodos da aplicação
Métodos de localizar elementos
Métodos condicionais
Métodos de interação com elementos
Métodos de espera


MÉTODOS DE NAVEGAÇÃO 
  browser.

  - get(): abre uma url
  - maximize_window(): Maximiza a tela
  - refresh(): atualiza página
  - back(): volta uma página
  - forward(): avança uma página
  - close(): fecha uma guia (separador)
  - quit(): mata o processo e fecha tudo

MÉTODOS DA APLICAÇÃO
  browser.

  - title: Titulo
  - current_url: Url
  - page_source: Código fonte

MÉTODOS PARA LOCALIZAR ELEMENTOS

  - find_element(): retorna a primeira ocorrencia e erro se não encontrar
  - find_elements(): retorna todas as ocorrencias e não retorna erro se não encontrar

MÉTODOS CONDICIONAIS 
  element.

  - is_displayed(): Diz se o elemento está sendo mostrado na tela ou não
  - is_enabled(): Diz se o elemento está habilitado ou não
  - is_selected(): Diz se o elemento está selecionado ou não

  Retorna True ou False

COMANDOS DE INTERAÇÃO COMELEMENTOS
  element.

  - click(): Clica em um elemento
  - send_keys(): Preenche campos de input
  - text: Pega o texto do elemento
  - get_attribute(): Pega o valor de um atributo do elemento

COMANDOS DE ESPERA (WAIT)
  element.

  - time.sleep()
  - implicitly_wait: 
  - explicitly_wait: 

  OBS.: Usar sleep() só em ultimo caso.

"""