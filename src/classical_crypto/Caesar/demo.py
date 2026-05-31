from .CaesarCipher import CaesarCipher
from .attack import brute_force


def encryption_demo():
    shift = 3
    plaintext = "HELLO WORLD"

    cipher = CaesarCipher(shift)

    ciphertext = cipher.encrypt(plaintext)
    decrypted = cipher.decrypt(ciphertext)

    print("=" * 50)
    print("ENCRYPTION / DECRYPTION DEMO")
    print("=" * 50)

    print(f"Shift      : {shift}")
    print(f"Plaintext  : {plaintext}")
    print(f"Ciphertext : {ciphertext}")
    print(f"Decrypted  : {decrypted}")


def brute_force_demo():
    ciphertext = "KHOOR ZRUOG"

    print("\n" + "=" * 50)
    print("BRUTE FORCE DEMO")
    print("=" * 50)

    print(f"Ciphertext: {ciphertext}\n")

    possibilities = brute_force(ciphertext)

    for shift, text in possibilities:
        print(f"Shift {shift:2}: {text}")


def main():
    encryption_demo()
    brute_force_demo()


if __name__ == "__main__":
    main()