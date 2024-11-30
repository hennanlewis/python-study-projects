from aes_cipher import AESCipher

def main():
    cipher = AESCipher(key_size=32)
    cipher
    text = "Texto confidencial aqui!"

    print("Texto original:", text)

    ciphertext, iv = cipher.encrypt(text)
    print(f"Texto encriptado (em bytes): {ciphertext}")

    decrypted_text = cipher.decrypt(ciphertext, iv)
    print(f"Texto decriptado: {decrypted_text}")

if __name__ == "__main__":
    main()
