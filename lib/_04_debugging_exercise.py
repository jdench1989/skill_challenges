# Return to this example and debug it using Discovery Debugging.

# If you can, forget about trying to solve it. Instead, discover as much as you can about what is going on in the program.

def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    # print(f"Original encrypted message is: {encrypted}")
    # print(f"Original key is: {key}")

    cipher = make_cipher(key)

    plaintext_chars = []
    # print('For loop begins:')
    for i in encrypted:
        plain_char = cipher[ord(i) - 65] #originally plain_char = cipher[65 - ord(i)] resulting in encrypting a second time rather than returning to original value
        # print(f"Character {i} decrypted to {plain_char}")
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(26)] #originally started at ASCII value 98 which is 'b' not 'a'
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")