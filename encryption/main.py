from icecream import ic
from aes_cipher import AESCipher

ic.configureOutput(prefix='DEBUG | ')

def main():
    cipher = AESCipher(key_size=32)
    plain_text = "Texto confidencial aqui!"
    ciphertext, iv = cipher.encrypt(plain_text)
    decrypted_text = cipher.decrypt(ciphertext, iv)

    ic(plain_text, ciphertext, decrypted_text)

if __name__ == "__main__":
    main()
