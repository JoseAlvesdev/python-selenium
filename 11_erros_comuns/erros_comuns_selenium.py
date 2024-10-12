"""
1. NoSuchElementException
  - Descrição: Ocorre quando o Selenium não consegue encontrar um elemento na página.
  - Causas:
    - O seletor utilizado está incorreto.
    - O elemento ainda não foi carregado na página.
    - O elemento foi removido ou não existe na página.

2. ElementNotInteractableException
  - Descrição: Ocorre quando o Selenium tenta interagir com um elemento que não está interagível.
  - Causas:
    - O elemento está oculto ou desabilitado.
    - O elemento está sobreposto por outro elemento (por exemplo, um modal ou um overlay).

3. StaleElementReferenceException
  - Descrição: Ocorre quando uma referência a um elemento não é mais válida, geralmente porque o DOM foi atualizado.
  - Causas:
    - O elemento foi removido ou alterado após ter sido encontrado.
    - A página foi recarregada ou alterada.

4. TimeoutException
  - Descrição: Ocorre quando uma operação (como esperar por um elemento) excede o tempo limite especificado.
  - Causas:
    - O elemento não aparece na página dentro do tempo limite.
    - A página leva muito tempo para carregar.

5. WebDriverException
  - Descrição: Exceção genérica para erros do WebDriver.
  - Causas:
    - Problemas de comunicação entre o Selenium e o navegador.
    - O navegador não está instalado ou não está acessível.

6. NoAlertPresentException
  - Descrição: Ocorre quando se tenta interagir com um alerta que não está presente.
  - Causas:
    - O código tenta aceitar ou rejeitar um alerta que não foi exibido.

7. ElementClickInterceptedException
  - Descrição: Ocorre quando um clique em um elemento é interceptado por outro elemento.
  - Causas:
    - Um elemento sobreposto (como um popup) impede a interação com o elemento desejado.

8. InvalidArgumentException
  - Descrição: Ocorre quando um argumento inválido é passado para um comando do Selenium.
  - Causas:
    - Um URL inválido é fornecido ao método get().
    - Parâmetros incorretos são passados para métodos.

9. JavascriptException
  - Descrição: Ocorre quando um erro é gerado ao executar um script JavaScript no contexto da página.
  - Causas:
    - O código JavaScript contém erros de sintaxe ou lógica.

10. ElementNotSelectableException
  - Descrição: Ocorre quando um elemento não pode ser selecionado.
  - Causas:
    - O elemento é um checkbox ou radio button que não está disponível para seleção.

Resumo
Esses erros são comuns ao trabalhar com Selenium e podem ocorrer em várias situações. Para lidar com eles:

  - Leia a documentação para entender melhor cada exceção.
  - Use blocos try-except para capturar e tratar essas exceções de forma adequada.
  - Teste seu código em diferentes cenários para identificar quais erros podem ocorrer e como preveni-los.
Com essa compreensão, você estará melhor preparado para depurar e tratar erros ao usar o Selenium em seus testes automatizados.
"""

try:
    return self.browser.find_element(*locator)

except NoSuchElementException as err:
    print(f'Elemento não encontrado: {err}')
    self.__close_browser()

except TimeoutException as err:
    print(f'Tempo limite de espera excedido: {err}')
    self.__close_browser()

except ElementNotInteractableException as err:
    print(f'Elemento não iterável: {err}')
    try:
        element: WebElement | None = self.__element(locator)
        if element:
            self.browser.execute_script('arguments[0].click()', element)
        else:
            raise NoSuchElementException
    except Exception as err:
        print(f'Tratamento interno: {err}')
        self.__close_browser()

except StaleElementReferenceException as err:
    print(f'Elemento não encontrado no DOM: {err}')
    try:
        sleep(2)
        return func(locator)
    except Exception as err:
        print(f'Tratamento interno: {err}')

except Exception as err:
    print(f'Erro inesperado: {err}')
    self.__close_browser()