from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

class AESCipher:
    def __init__(self, key_size=32):
        """
        Inicializa a classe AESCipher com uma chave gerada aleatoriamente.

        Args:
            key_size (int): O tamanho da chave em bytes. Pode ser 16, 24 ou 32.
        """
        if key_size not in [16, 24, 32]:
            raise ValueError("O tamanho da chave deve ser 16, 24 ou 32 bytes.")
        self.key = os.urandom(key_size)
        self.key_size = key_size

    def encrypt(self, plaintext):
        """
        Encripta o texto usando AES no modo CBC.

        Args:
            plaintext (str): O texto a ser encriptado.

        Returns:
            tuple: O texto encriptado (bytes) e o vetor de inicialização (IV).
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())


        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()

        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        return ciphertext, iv

    def decrypt(self, ciphertext, iv):
        """
        Decripta o texto encriptado usando AES no modo CBC.

        Args:
            ciphertext (bytes): O texto encriptado.
            iv (bytes): O vetor de inicialização (IV).

        Returns:
            str: O texto decriptado.
        """
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())

        # Decripta o texto
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Remove o padding
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        return plaintext.decode()

    def get_key(self):
        """Retorna a chave usada para encriptação."""
        return self.key

