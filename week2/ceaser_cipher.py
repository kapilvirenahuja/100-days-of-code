alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shift):
    encrypted_message = ""
    for letter in message:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            encrypted_message += alphabet[(letter_index + shift) % len(alphabet)]
        else:
            encrypted_message += letter
    print(f"The encoded text is -> {encrypted_message}")

def decrypt(message, shift):
    decrypted_message = ""
    for letter in message:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            decrypted_message += alphabet[(letter_index - shift) % len(alphabet)]
        else:
            decrypted_message += letter
    print(f"The decoded text is -> {decrypted_message}")


action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if action == "encode":
    encrypt(message, shift)
elif action == "decode":
    decrypt(message, shift)
else:
    print("Invalid action. Please try again.")

# Output:
# Type 'encode' to encrypt, type 'decode' to decrypt:
# encode
# Type your message:
# hello
# Type the shift number:
# 5

# The encoded text is mjqqt
