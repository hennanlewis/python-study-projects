# Gerenciador de Impressoras

Este projeto oferece uma ferramenta para gerenciar impressoras conectadas ao sistema Windows. Ele utiliza a biblioteca `pywin32` para acessar informações detalhadas sobre as impressoras e realizar ações como listar, verificar e manipular portas de impressoras.

## Funcionalidades

- **Listagem de Impressoras**: Recupera a lista de impressoras instaladas no sistema, incluindo detalhes sobre cada uma.
- **Consulta de Portas**: Permite consultar as portas associadas a uma impressora específica.
- **Validação de Portas**: Verifica se uma porta específica existe para uma impressora.
- **Manipulação de Portas**: Oferece métodos para criar, alterar e excluir portas de impressoras.

## Instalação

### Pré-requisitos

Certifique-se de estar em um sistema operacional Windows. Utilize o Poetry ou o pip para a instalação dos pacotes.

Caso precise de ajuda, veja o passo a passo de como executar os projetos python deste repositório [aqui](../doc/UsandoProjetos.md).


## Uso

### Exemplo de uso:

```python
from printer_manager import PrinterManager

# Inicializar o PrinterManager
printer_manager = PrinterManager()

# Listar os nomes de todas as impressoras instaladas
printers = printer_manager.printers_names
print("Lista de Impressoras:", printers)

# Verificar os detalhes de todas as impressoras
printers_details = printer_manager.printers_details
print("Detalhes das impressoras:", printers_details)

# Verificar as portas disponíveis no sistema
printers_ports = printer_manager.printers_ports
print("Portas disponíveis:", printers_ports)

# Verificar se uma porta específica existe
port_name = "COM1"
exists = printer_manager.check_port_exists(port_name)
print(f"A porta {port_name} existe: {exists}")

# Criar uma nova porta TCP/IP
new_port_name = "NovaPorta"
new_port_ip = "192.168.1.100"
try:
    result = printer_manager.create_ip_port(new_port_name, new_port_ip)
    print(result)
except RuntimeError as e:
    print(f"Erro ao criar a porta {new_port_name}: {e}")

# Excluir uma porta
try:
    result = printer_manager.delete_port(new_port_name)
    print(result)
except RuntimeError as e:
    print(f"Erro ao excluir a porta {new_port_name}: {e}")
```

### Métodos Disponíveis

`PrinterManager.printers_names`
- **Descrição**: Lista apenas os nomes das impressoras instaladas.
- **Parâmetros**: Nenhum.
- **Retorno**: Uma lista de strings contendo os nomes das impressoras.

`PrinterManager.printers_details`
- **Descrição**: Detalhes completos das impressoras instaladas.
- **Parâmetros**: Nenhum.
- **Retorno**: Uma lista de dicionários com informações detalhadas de cada impressora.

`PrinterManager.printers_ports`
- **Descrição**: Lista as portas associadas às impressoras disponíveis.
- **Parâmetros**: Nenhum.
- **Retorno**: Uma lista de dicionários contendo informações das portas.

`PrinterManager.check_port_exists(port_name)`
- **Descrição**: Verifica se uma porta específica existe no sistema.
Parâmetros:
    - `port_name` (str): Nome da porta a ser verificada.
- **Retorno**: Um valor booleano indicando a existência da porta.

`PrinterManager.create_ip_port(port_name, port_value)`
- **Descrição**: Cria uma nova porta TCP/IP.
Parâmetros:
    - `port_name` (str): Nome da nova porta.
    - `port_value` (str): Endereço IP associado à porta.
- **Retorno**: Uma mensagem indicando sucesso ou erro.

`PrinterManager.delete_port(port_name)`
- **Descrição**: Exclui uma porta especificada.
Parâmetros:
    - `port_name` (str): Nome da porta a ser excluída.
- **Retorno**: Uma mensagem indicando sucesso ou erro.


## Considerações

- **Permissões Administrativas**: Certifique-se de executar o script com permissões administrativas para evitar erros relacionados a permissões.
- **Validação Prévia**: Sempre verifique os nomes das impressoras e portas antes de realizar ações para evitar problemas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias ou correções.
