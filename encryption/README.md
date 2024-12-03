# AESCipher - Criptografia AES

Este projeto implementa a criptografia e decriptação de dados utilizando o algoritmo AES (Advanced Encryption Standard) em modo CBC (Cipher Block Chaining). Ele inclui suporte a padding (PKCS7) para garantir que os dados sejam adequadamente ajustados ao tamanho do bloco do AES.

## Funcionalidades

- **Criptografia AES** (CBC): Encripta dados usando a chave AES no modo CBC.
- **Decriptação AES** (CBC): Desencripta dados encriptados com AES no modo CBC.
- **Padding** (PKCS7): Adiciona e remove o padding de dados para garantir que o texto tenha o tamanho correto (múltiplo de 16 bytes) antes da encriptação e após a decriptação.
- **Validações Robustas**: Verificações para garantir a integridade de entradas e evitar erros comuns (como tamanhos incorretos de IV ou chaves).
- **Separação de Lógica**: Métodos dedicados para geração de chaves e vetores de inicialização (IVs), facilitando testes e reutilização.

## Constantes

- `DEFAULT_KEY_SIZE` (int): Tamanho padrão da chave AES em bytes (32 bytes).
- `AES_BLOCK_SIZE` (int): Tamanho do bloco AES em bytes (16 bytes).

## Instalação

Utilize o Poetry ou o pip para a instalação dos pacotes.

Caso precise de ajuda, veja o passo a passo de como executar os projetos python deste repositório [aqui](../doc/UsandoProjetos.md).

## Uso

### Exemplo de uso:

```python
from aes_cipher import AESCipher

# Criação de um objeto AESCipher
cipher = AESCipher()

# Texto a ser encriptado
plaintext = "Mensagem secreta"

# Criptografando o texto
ciphertext, iv = cipher.encrypt(plaintext)
print(f"Texto encriptado: {ciphertext}")

# Desencriptando o texto
decrypted_text = cipher.decrypt(ciphertext, iv)
print(f"Texto decriptado: {decrypted_text}")
```

### Métodos disponíveis:

#### `encrypt(plaintext: str) -> Tuple[bytes, bytes]`
- **Descrição**: Criptografa o texto fornecido usando AES em modo CBC, com padding PKCS7.
- **Parâmetros**:
    - `plaintext` (str): O texto que você deseja encriptar.
- **Retorno**: Retorna o texto encriptado (`ciphertext`) e o vetor de inicialização (`iv`) usados.
- **Validação**: Garante que o `plaintext` seja do tipo `str`.

#### `decrypt(ciphertext: bytes, iv: bytes) -> str`
- **Descrição**: Desencripta o texto fornecido usando AES em modo CBC, removendo o padding PKCS7.
- **Parâmetros**:
    - `ciphertext` (bytes): O texto encriptado que você deseja decriptar.
    - `iv` (bytes): O vetor de inicialização usado na encriptação.
- **Retorno**: Retorna o texto decriptado como uma string (`str`).
- **Validações**:
    - Garante que `ciphertext` e `iv` sejam do tipo `bytes`.
    - Verifica se o `iv` tem o tamanho correto (`AES_BLOCK_SIZE`).

#### `get_key() -> bytes`
- **Descrição**: Retorna a chave de encriptação usada pelo objeto.
- **Retorno**: A chave AES.

#### `_generate_key(key_size: int) -> bytes`
- **Descrição**: Gera uma chave AES aleatória do tamanho especificado.
- **Parâmetros**:
    - `key_size` (int): Tamanho da chave em bytes.
- **Retorno**: Chave AES gerada.

#### `_generate_iv() -> bytes`
- **Descrição**: Gera um vetor de inicialização (IV) aleatório.
- **Retorno**: Vetor de inicialização (`IV`).

### Métodos internos:

- `_add_padding(data: bytes) -> bytes`: Adiciona o padding (PKCS7) ao texto.
- `_remove_padding(data: bytes) -> bytes`: Remove o padding (PKCS7) do texto.

## Como o Padding Funciona?

A criptografia AES, em particular no modo CBC, exige que o texto a ser encriptado tenha um tamanho que seja um múltiplo do tamanho do bloco (16 bytes). Quando o texto não tem esse tamanho, padding é adicionado para preencher o texto até o tamanho adequado.

O padding é feito utilizando o padrão PKCS7, que adiciona bytes no final do texto com um valor que indica quantos bytes foram adicionados. Por exemplo:

- Se o texto tem 13 bytes e o AES espera 16, serão adicionados 3 bytes de padding (`\x03\x03\x03`).

Após a decriptação, o padding é removido para que o texto original seja restaurado.

## Considerações de Segurança

- Chave AES: A chave AES é gerada aleatoriamente ao criar uma instância da classe `AESCipher`. Certifique-se de armazenar a chave de forma segura se você precisar de persistência para encriptação e decriptação futuros.
- Vetor de Inicialização (IV): O IV é gerado aleatoriamente a cada encriptação e deve ser armazenado junto com o texto encriptado. Ele não precisa ser mantido em segredo, mas deve ser único para cada operação de encriptação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com suas melhorias ou correções.
