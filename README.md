# Python Study Projects
Repositório que concentra projetos para estudos em python

# Requisitos

- Python 3.x instalado
- Git instalado (recomendado)
- Poetry instalado (recomendado)

### Python

Para maior compatibilidade, tenha o `python 3.12` instalado no seu computador. Você pode obtê-lo [aqui](https://www.python.org/downloads/).

## Poetry

O Poetry é uma ferramenta moderna para gerenciamento de dependências e empacotamento de projetos Python. Ele facilita a instalação e o gerenciamento de pacotes, a criação de ambientes virtuais, e a distribuição de projetos Python de maneira simplificada e consistente.

Para mais informações de como instalar o Poetry, clique [aqui](https://python-poetry.org/docs/#installing-with-the-official-installer).

### Git

O Git é um sistema de controle de versão distribuído e open-source (código aberto) usado para rastrear mudanças no código-fonte durante o desenvolvimento de software. Ele permite que desenvolvedores colaborem em projetos de forma eficiente, mantendo um histórico completo das alterações feitas nos arquivos e facilitando o gerenciamento de versões de software.

Para mais informações de como instalar o Git, clique [aqui](https://git-scm.com/downloads).

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

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias ou correções.
