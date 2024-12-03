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

# Listar todas as impressoras instaladas
printers = PrinterManager.get_printer_list()
print("Lista de Impressoras:", printers)

# Verificar as portas de uma impressora específica
printer_name = "Nome da Impressora"
ports = PrinterManager.get_ports(printer_name)
print(f"Portas da impressora {printer_name}:", ports)

# Verificar se uma porta específica existe
port_name = "COM1"
exists = PrinterManager.check_port_exists(printer_name, port_name)
print(f"A porta {port_name} existe para a impressora {printer_name}: {exists}")

# Criar uma nova porta para uma impressora
result = PrinterManager.create_port(printer_name, "NovaPorta", "Valor")
print(result)

# Alterar o valor de uma porta existente
result = PrinterManager.set_port_value(printer_name, "NovaPorta", "NovoValor")
print(result)

# Excluir uma porta de uma impressora
result = PrinterManager.delete_port(printer_name, "NovaPorta")
print(result)
```

### Métodos Disponíveis

`PrinterManager.get_printer_list()`
- **Descrição**: Retorna a lista de impressoras instaladas no sistema.
- **Parâmetros**: Nenhum.
- **Retorno**: Uma lista de dicionários contendo informações detalhadas de cada impressora.

`PrinterManager.get_ports(printer_name)`
- **Descrição**: Recupera as portas associadas a uma impressora específica.
- **Parâmetros**:
  - `printer_name` (str): Nome da impressora.
- **Retorno**: Uma lista de portas ou uma mensagem de erro.

`PrinterManager.check_port_exists(printer_name, port_name)`
- **Descrição**: Verifica se uma porta específica existe para a impressora fornecida.
- **Parâmetros**:
  - `printer_name` (str): Nome da impressora.
  - `port_name` (str): Nome da porta a ser verificada.
- **Retorno**: Um valor booleano indicando a existência da porta.

`PrinterManager.set_port_value(printer_name, port_name, value, monitor=None)`
- **Descrição**: Altera o valor de uma porta específica.
- **Parâmetros**:
  - `printer_name` (str): Nome da impressora.
  - `port_name` (str): Nome da porta.
  - `value` (str): Novo valor para a porta.
  - `monitor` (str, opcional): Monitor associado à porta.
- **Retorno**: Uma mensagem indicando sucesso ou erro.

`PrinterManager.create_port(printer_name, port_name, value, monitor=None)`
- **Descrição**: Cria uma nova porta para a impressora especificada.
- **Parâmetros**: Mesmo que `set_port_value`.

`PrinterManager.delete_port(printer_name, port_name)`
- **Descrição**: Exclui uma porta de uma impressora, se existente.
- **Parâmetros**:
  - `printer_name` (str): Nome da impressora.
  - `port_name` (str): Nome da porta a ser excluída.
- **Retorno**: Uma mensagem indicando sucesso ou erro.

## Considerações

- **Permissões Administrativas**: Certifique-se de executar o script com permissões administrativas para evitar erros relacionados a permissões.
- **Validação Prévia**: Sempre verifique os nomes das impressoras e portas antes de realizar ações para evitar problemas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias ou correções.
