# Utilizando os projetos

Para utilizar os projetos deste repositório, primeiro você precisa entrar na pasta do projeto, instalar os pacotes necessários e depois executar o código:

## Instalando e executando

### Com Poetry (recomendado)

1. Clone o repositório com o git:
```shell
git clone https://github.com/hennanlewis/python-projets.git
```
Ou baixe o arquivo `.zip` do projeto [aqui](https://github.com/hennanlewis/python-projects/archive/refs/heads/main.zip).

2. Entre na pasta do repositório por linha de comando e na pasta do projeto desejado e instale os múdulos necessários:
```bash
cd python-projects/<nome da pasta do projeto>
poetry install
```

3. Após os múdulos instalarem, execute o projeto:
```bash
poetry shell
python main.py
```

4. Após executar o projeto, finaliza a utilização do ambiente do Poetry com o seguinte código:
```bash
deactivate
```

### Com python

1. Clone o repositório com o git
```shell
git clone https://github.com/hennanlewis/python-projets.git
```
Ou baixe o arquivo `.zip` do projeto [aqui](https://github.com/hennanlewis/python-projects/archive/refs/heads/main.zip).

2. Entre na pasta do repositório por linha de comando e na pasta do projeto desejado:
```bash
cd python-projects/<nome da pasta do projeto>
```

3. Crie um ambient vitual por linha de comando na pasta do projeto
```shell
# No Linux:
python -m venv .env
source .env/bin/activate

# No Windows
python -m venv .env
.env\Scripts\activate
```

4. Instale os pacotes necessários:
```shell
pip install -r requirements.txt
```

5. Após os múdulos instalarem, execute o projeto:
```bash
python main.py
```

6. Para finalizar o uso do ambiente, utilize o seguinte código:
```shell
deactivate
```
