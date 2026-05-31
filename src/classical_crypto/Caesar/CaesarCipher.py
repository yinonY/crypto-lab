class CaesarCipher:

    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            new_char = self._shift_character(char, self.shift)
            encrypted_text += new_char.upper()
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            new_char = self._shift_character(char, -self.shift)
            decrypted_text += new_char.lower()
        return decrypted_text

    def brute_force(self, ciphertext):
        all_decryptions = []
        for i in range(26):
            shi
            decrypted_text = ""
            for char in ciphertext:
                decrypted_text = d
                
        

    def _shift_character(self, char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        else:
            return char