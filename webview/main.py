import os
import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import json
import base64

# Função para gerar chave a partir da URL (usando SHA-256 para garantir uma chave de 256 bits)
def generate_key_from_url(url):
    from hashlib import sha256
    return sha256(url.encode()).digest()

# Função para criptografar dados
def encrypt_data(data, key):
    # Inicializando o modo de cifra (AES CBC)
    iv = os.urandom(16)  # Vetor de inicialização aleatório
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Adicionando padding para que o tamanho dos dados seja múltiplo do tamanho do bloco (16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    # Criptografando os dados
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Retorna os dados criptografados junto com o vetor de inicialização (IV) base64 codificado
    return base64.b64encode(iv + encrypted_data).decode()

# Função para descriptografar dados
def decrypt_data(encrypted_data, key):
    encrypted_data = base64.b64decode(encrypted_data)

    # Extraindo o vetor de inicialização (IV) e os dados criptografados
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    # Inicializando a cifra para descriptografar
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografando os dados
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Removendo o padding
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(decrypted_data) + unpadder.finalize()

class WebWindow(QMainWindow):
    def __init__(self, url, title, icon):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon(icon))

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)

def fetch_website_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Obtendo o título da página
        start_title = response.text.find('<title>') + len('<title>')
        end_title = response.text.find('</title>', start_title)
        title = response.text[start_title:end_title]

        # Obtendo o ícone da página (se existir)
        icon_url = None

        # Verificando 'shortcut icon'
        start_icon = response.text.find('<link rel="shortcut icon" href="') + len('<link rel="shortcut icon" href="')
        if start_icon != -1:
            end_icon = response.text.find('"', start_icon)
            icon_url = response.text[start_icon:end_icon]

        # Se não encontrar o "shortcut icon", verifica o "icon"
        if not icon_url:
            start_icon = response.text.find('<link rel="icon" href="') + len('<link rel="icon" href="')
            if start_icon != -1:
                end_icon = response.text.find('"', start_icon)
                icon_url = response.text[start_icon:end_icon]

        if icon_url:
            # Se o ícone não for uma URL absoluta, adiciona a base da URL
            if not icon_url.startswith("http"):
                icon_url = url + icon_url

            icon_response = requests.get(icon_url, stream=True)
            icon_path = "favicon.ico"
            with open(icon_path, 'wb') as f:
                f.write(icon_response.content)

            return title, icon_path
        else:
            return title, "default_icon.ico"
    except Exception as e:
        print(f"Erro ao obter dados do site: {e}")
        return "Erro", "default_icon.ico"

def create_config_file(url, title, icon):
    config_data = {
        "url": url,
        "title": title,
        "icon": icon
    }

    # Gerar chave a partir da URL
    key = generate_key_from_url(url)

    # Criptografar os dados antes de salvar
    encrypted_data = encrypt_data(json.dumps(config_data), key)

    # Salvar os dados criptografados em um arquivo sem extensão
    with open("config", "w") as config_file:
        config_file.write(encrypted_data)

def read_config_file():
    if os.path.exists("config"):
        with open("config", "r") as config_file:
            return config_file.read()
    return None

def main():
    # Tenta carregar o arquivo "info"
    try:
        with open("info", "r") as file:
            url = file.readline().strip()
    except FileNotFoundError:
        print("Arquivo 'info' não encontrado.")
        return

    # Verificar se o arquivo de configuração já existe e se está vazio
    encrypted_config = read_config_file()

    if encrypted_config:
        if encrypted_config.strip():  # Verifica se o conteúdo não está vazio
            # O arquivo de configuração existe e não está vazio, então descriptografa os dados
            key = generate_key_from_url(url)
            decrypted_data = decrypt_data(encrypted_config, key)
            config = json.loads(decrypted_data)
            url = config["url"]
            title = config["title"]
            icon = config["icon"]
        else:
            # Se o arquivo de configuração está vazio, faz a requisição normalmente
            title, icon = fetch_website_data(url)

            # Cria o arquivo de configuração com os dados obtidos
            create_config_file(url, title, icon)
    else:
        # O arquivo de configuração não existe, então faz a requisição e cria o arquivo
        title, icon = fetch_website_data(url)

        # Cria o arquivo de configuração com os dados obtidos
        create_config_file(url, title, icon)

    # Cria a aplicação PyQt e abre a janela
    app = QApplication([])
    window = WebWindow(url, title, icon)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
