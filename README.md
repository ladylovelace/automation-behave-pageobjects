# automation-behave-pageobjects
Automation with Python, Behav, Selenium using desing pattern Page Objects

## Requisitos

Após clonar o projeto, é necessário acertar o arquivo de configuração. Crie uma cópia do arquivo ```config.py.dist``` com o nome ```config.py``` e altere como precisar.

    cp features/config.py{.dist,}

Cheque se possui o pip3, caso contrário:

    $ [sudo] pip3 install virtualenv

Cheque a versão do pyhton que está instalado com:
	
	$ python --version

Caso seja a versão python2.7+, vc precisa instalar o python-pip3 com:
	
	$ [sudo] apt install python3-pip

Caso sua versão seja python3.5+, vc precisa instalar o python-pip com:

	$ [sudo] apt install python-pip
---

### Virtualenv

O virtualenv permite ter um ambiente python isolado para o projeto. É fortemente recomendável o seu uso em máquina local. 

    $ virtualenv -p python3 venv
    $ . ./venv/bin/activate

> Dica: Utilize o virtualenv com o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

---

### Instalando dependências
Para realizar a instalação das dependências basta executar o comando após entrar na sua máquina virtual:

    (venv)$ pip install -r requirements.txt
---

### Executando
Para executar todos os cenários:

    (venv)$ behave

Para executar apenas cenários taggeados (@sunny, por exemplo):

    (venv)$ behave --tags=sunny

Para executar uma feature:

    (venv)$ behave features/tweet.feature
---

### Headless

Para executar a automação em modo *headless*, basta descomentar a seguinte linha de código no arquivo `./features/lib/pages/browser.py`. Esse tipo de automação roda em segundo plano e 'libera' a continuação do uso do computador:

    # chrome_options.add_argument("--headless")

Este projeto foi desenvolvido em `python3+`, [selenium3.11+](http://selenium-python.readthedocs.io/) e [behave](https://behave.readthedocs.io/en/latest/)
