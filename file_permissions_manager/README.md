# Gerenciador de Permissões de Arquivos e Diretórios

Este projeto fornece uma ferramenta para gerenciar permissões de arquivos e diretórios no Windows. Ele utiliza os comandos takeown e icacls para alterar o proprietário e definir permissões de forma programática.
Funcionalidades

- **Alteração Individual de Permissões**: Modifica as permissões de arquivos e diretórios de forma individual.
- **Alteração em Lote de Permissões**: Modifica permissões de todos os arquivos e subdiretórios de forma recursiva.
- **Geração de Logs**: Registra arquivos com sucesso e falha em arquivos separados (`success_files.txt` e `failure_files.txt`).
- **Opção de Processamento**: Escolha entre alterar permissões individualmente ou em lote.

## Instalação

Certifique-se de estar em um sistema operacional Windows com permissões administrativas para executar comandos como `takeown` e `icacls`.
Utilize o Poetry ou o pip para a instalação dos pacotes.

Caso precise de ajuda, veja o passo a passo de como executar os projetos python deste repositório [aqui](../doc/UsandoProjetos.md).

## Uso

### Exemplo de Uso

```python
from permission_manager import PermissionManager

# Definir o diretório que será processado
path_to_process = r"E:\Windows\System32"

# Criar uma instância do PermissionManager
permission_manager = PermissionManager(path_to_process)

# Processar permissões de forma individual
permission_manager.process_directory(use_bulk=False)

# Processar permissões de forma em lote
permission_manager.process_directory(use_bulk=True)
```
### Métodos Disponíveis

`PermissionManager.__init__(directory: str)`
- **Descrição**: Inicializa o gerenciador para o diretório especificado.
- **Parâmetros**:
    - `directory` (str): Caminho do diretório a ser processado.
- **Retorno**: Nenhum.

`PermissionManager.process_directory(use_bulk: bool = False)`
- **Descrição**: Processa permissões no diretório especificado.
- **Parâmetros**:
    - `use_bulk` (bool): Determina se o processamento será individual (`False`) ou em lote (`True`).
- **Retorno**: Nenhum.

### Métodos Internos

- `_change_permissions(file_path: str)`: Altera permissões de um único arquivo ou diretório.
- `_change_permissions_bulk(directory: str)`: Altera permissões de todos os arquivos e subdiretórios recursivamente.
- `_log_result(file_path: str, is_success: bool)`: Registra o sucesso ou falha do processamento em arquivos de log.

## Logs Gerados

O script cria dois arquivos de log:

- `success_files.txt`: Lista arquivos e diretórios com permissões alteradas com sucesso.
- `failure_files.txt`: Lista arquivos e diretórios onde houve falha na alteração de permissões.

## Considerações de Segurança

- **Permissões Administrativas**: Certifique-se de executar o script com permissões administrativas.
- **Impacto em Diretórios Sensíveis**: Tenha cuidado ao usar o script em diretórios sensíveis do sistema, como `System32`, pois alterações inadequadas podem causar problemas no sistema operacional.
- **Backup**: Faça backup de seus dados antes de executar o script, especialmente em diretórios críticos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias ou correções.
