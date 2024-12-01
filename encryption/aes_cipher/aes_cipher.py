from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
from typing import Tuple

class AESCipher:
    def __init__(self, key: bytes = None, key_size: int = 32):
        """Inicializa a classe com uma chave AES gerada aleatoriamente."""

        if key_size not in [16, 24, 32]:
            raise ValueError("O tamanho da chave deve ser 16, 24 ou 32 bytes.")

        self.key = key or os.urandom(key_size)
        self.key_size = key_size

    def encrypt(self, plaintext: str) -> Tuple[bytes, bytes]:
        """Encripta o texto em modo CBC."""
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        padded_plaintext = self._add_padding(plaintext.encode())
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        return ciphertext, iv

    def decrypt(self, ciphertext: bytes, iv: bytes) -> str:
        """Decripta o texto encriptado em modo CBC."""
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        plaintext = self._remove_padding(padded_plaintext)

        return plaintext.decode()

    def get_key(self) -> bytes:
        """Retorna a chave de encriptação usada."""
        return self.key

    @staticmethod
    def _add_padding(data: bytes) -> bytes:
        """Adiciona padding ao dado para alinhá-lo ao tamanho do bloco."""
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        return padder.update(data) + padder.finalize()

    @staticmethod
    def _remove_padding(data: bytes) -> bytes:
        """Remove o padding dos dados."""
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        return unpadder.update(data) + unpadder.finalize()
