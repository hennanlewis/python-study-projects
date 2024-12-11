# EasyImageEditor

Este projeto é uma ferramenta simples e eficiente para editar imagens, permitindo adicionar imagens sobrepostas e textos personalizados em posições específicas. Ideal para composições rápidas e ajustáveis.

## Funcionalidades

- **Inserção de Imagens**: Sobrepõe imagens em outras, com ajuste de posição e redimensionamento automático.
- **Adição de Textos**: Adiciona textos em qualquer posição da imagem, com suporte a fontes locais.
- **Processamento em Lote**: Permite editar várias imagens de uma vez, mantendo o controle individual sobre cada operação.
- **Interface Simples**: Oferece um menu interativo para selecionar operações e ajustar parâmetros.

## Instalação

Utilize o Poetry ou o pip para a instalação dos pacotes.

Caso precise de ajuda, veja o passo a passo de como executar os projetos python deste repositório [aqui](../doc/UsandoProjetos.md).

## Uso

### Exemplo de Uso

```python
from easy_image_editor import EasyImageEditor

# Configurar os caminhos
input_folder = "Primárias"
output_folder = "Finais"
overlay_image_path = "channel name.png"

# Criar uma instância do editor
editor = EasyImageEditor(input_folder, output_folder, overlay_image_path)

# Inserir uma imagem sobreposta em todas as imagens da pasta
editor.add_overlay_to_all()

# Inserir texto em uma imagem específica
editor.add_text_to_image(
    image_name="exemplo.jpg",
    text="Hello, World!",
    position=(50, 50),
    font_path="arial.ttf",
    font_size=24
)
```

### Métodos Disponíveis

#### `EasyImageEditor.__init__(input_folder: str, output_folder: str, overlay_image_path: str)`
- **Descrição**: Inicializa o editor para as operações de edição.
- **Parâmetros**:
    - `input_folder` (str): Caminho da pasta de entrada com as imagens a serem editadas.
    - `output_folder` (str): Caminho da pasta de saída para salvar as imagens editadas.
    - `overlay_image_path` (str): Caminho da imagem que será usada como sobreposição.
- **Retorno**: Nenhum.

#### `add_overlay_to_all()`
- **Descrição**: Adiciona a imagem de sobreposição a todas as imagens na pasta de entrada.
- **Parâmetros**: Nenhum.
- **Retorno**: Nenhum.

#### `add_overlay_to_image(image_name: str, position: tuple = None)`
- **Descrição**: Adiciona a imagem de sobreposição em uma imagem específica.
- **Parâmetros**:
    - `image_name` (str): Nome do arquivo da imagem a ser editada.
    - `position` (tuple, opcional): Posição (x, y) da sobreposição. Padrão é o topo esquerdo.
- **Retorno**: Nenhum.

#### `add_text_to_image(image_name: str, text: str, position: tuple, font_path: str, font_size: int)`
- **Descrição**: Adiciona texto a uma imagem específica.
- **Parâmetros**:
    - `image_name` (str): Nome do arquivo da imagem a ser editada.
    - `text` (str): Texto a ser adicionado.
    - `position` (tuple): Posição (x, y) do texto na imagem.
    - `font_path` (str): Caminho para a fonte a ser usada.
    - `font_size` (int): Tamanho da fonte.
- **Retorno**: Nenhum.

## Logs Gerados

O script gera logs para acompanhar as operações realizadas:

- `edited_images.txt`: Lista imagens que foram editadas com sucesso.
- `error_log.txt`: Lista erros ocorridos durante o processamento.

## Considerações de Uso

- **Fontes Locais**: Certifique-se de que as fontes usadas estejam instaladas ou disponíveis no caminho especificado.
- **Backup de Imagens**: Recomendamos fazer backup das imagens antes de editar, especialmente se estiver processando em lote.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com melhorias, novos recursos ou correções de bugs.
