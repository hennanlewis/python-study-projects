from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
from typing import Tuple

# Definição de constantes para melhorar legibilidade e manutenção
DEFAULT_KEY_SIZE = 32
AES_BLOCK_SIZE = 16

class AESCipher:
    def __init__(self, key: bytes = None, key_size: int = DEFAULT_KEY_SIZE):
        """Inicializa a classe com uma chave AES."""

        if key_size not in [16, 24, 32]:
            raise ValueError("O tamanho da chave deve ser 16, 24 ou 32 bytes.")
        self.key = key or self._generate_key(key_size)

    def encrypt(self, plaintext: str) -> Tuple[bytes, bytes]:
        """Encripta o texto em modo CBC."""

        if not isinstance(plaintext, str):
            raise TypeError("O plaintext deve ser uma string.")

        iv = self._generate_iv()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        padded_plaintext = self._add_padding(plaintext.encode())
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        return ciphertext, iv

    def decrypt(self, ciphertext: bytes, iv: bytes) -> str:
        """Decripta o texto encriptado em modo CBC."""

        if not isinstance(ciphertext, bytes) or not isinstance(iv, bytes):
            raise TypeError("Ciphertext e IV devem ser do tipo bytes.")
        if len(iv) != AES_BLOCK_SIZE:
            raise ValueError(f"O IV deve ter {AES_BLOCK_SIZE} bytes.")

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

    @staticmethod
    def _generate_key(key_size: int) -> bytes:
        """Gera uma chave AES aleatória."""

        return os.urandom(key_size)

    @staticmethod
    def _generate_iv() -> bytes:
        """Gera um vetor de inicialização (IV) aleatório."""

        return os.urandom(AES_BLOCK_SIZE)
