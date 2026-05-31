from .CaesarCipher import CaesarCipher

def brute_force(cipher_text):
    results = []

    for key in range(26):
        decrypted_text = CaesarCipher(key).decrypt(cipher_text)
        results.append((key, decrypted_text))

    return results