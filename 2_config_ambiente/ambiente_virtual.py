"""
O QUE É UM AMBIENTE VITUAL?
  É um ambiente que vc instala as dependências de um projeto, e essas 
  depêndencias ficarão isoladas somente naquele projeto.

  Evita que as dependências entrem em comflito.

  link uteis:
  art: https://python.land/virtual-environments/virtualenv
  vid: https://youtu.be/fEn5cnYnDnI?si=BWmkeh_QgoKxlMFG

PASSOS
  1 - Estar na pasta do projeto

  2 - Já na pasta do projeto, abra um terminal e execute:
    python -m venv venv
    python -m venv [nome_venv]

Como criar no VsCode?
  No vs code você precisa ativar manualmente o ambiente

  1 - No terminal execute: venv_name/Scripts/Activate.ps1 (PwShell)

  OBS.: No terminal do windows (cmd) use activate.bat

  OBS.: No terminal do GitHub (bash) usar: 
  
    active -> source venv_name/Scripts/activate

  2 - Como desativar tanto no windows tanto no linux/bash

    $ deactivate

Como criar no PyCharm?
  1 - Criar um novo projeto, e o ambiente virtual e criado automáticamente.
  OBS.: Más caso precise criar um o tutorial é o mesmo.
"""