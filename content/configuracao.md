# Instalação e configuração do projeto

Antes de mais nada precisamos fazer o download do projeto na máquina local e 
fazer as devidas configurações.

Escolha o diretório na sua máquina onde o projeto `Connect4-Python` deve ser armazenado
e faça o clone do projeto: 

```bash
git clone git@github.com:fbarth/Connect4-Python.git
```

Como sempre, sugerimos criar um ambiente virtual para garantir que todas as dependências 
sejam as corretas: 

```bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Uma vez que o projeto está instalado e o ambiente virtual configuração então podemos ir
para a próxima [parte](parte1.md).