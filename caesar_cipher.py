def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
            
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

print("Welcome to the Caesar Cipher Program!")
choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

if choice == 'e':
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher_encrypt(text, shift)
    print("Encrypted Text:", encrypted_text)
    print("Your text was successfully encrypted.")
    
elif choice == 'd':
    text = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted_text = caesar_cipher_decrypt(text, shift)
    print("Decrypted Text:", decrypted_text)
    print("Your text was successfully decrypted.")
    
else:
    print("Invalid choice, please enter 'e' or 'd'.")
