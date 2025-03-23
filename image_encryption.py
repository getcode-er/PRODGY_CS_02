import cv2
import numpy as np

def encrypt_image(image_path, key):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    encrypted_img = (img.astype(np.uint16) + key) % 256  # Convert to uint16 to prevent overflow
    encrypted_img = encrypted_img.astype(np.uint8)  # Convert back to uint8 for saving
    
    cv2.imwrite("encrypted_image.png", encrypted_img)
    print("Encryption complete! Saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    img = cv2.imread(encrypted_image_path)
    if img is None:
        print("Error: Encrypted image not found!")
        return
    
    decrypted_img = (img.astype(np.uint16) - key) % 256  # Convert to uint16 for safe subtraction
    decrypted_img = decrypted_img.astype(np.uint8)  # Convert back to uint8
    
    cv2.imwrite("decrypted_image.png", decrypted_img)
    print("Decryption complete! Saved as 'decrypted_image.png'.")

if __name__ == "__main__":
    print("Image Encryption Tool")
    choice = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if choice == "encrypt":
        img_path = input("Enter the image path: ").strip()
        key = int(input("Enter encryption key (1-255): "))
        encrypt_image(img_path, key)

    elif choice == "decrypt":
        img_path = input("Enter the encrypted image path: ").strip()
        key = int(input("Enter decryption key (same as encryption key): "))
        decrypt_image(img_path, key)

    else:
        print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
