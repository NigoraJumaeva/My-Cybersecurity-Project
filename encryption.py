# Data Encryption Tool - Practice Demo
# Implements Caesar Cipher and Fernet (symmetric encryption)

try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except Exception as e:
    CRYPTO_AVAILABLE = False
    print("Optional dependency 'cryptography' not installed. Install with: pip install cryptography")

def caesar_encrypt(text, shift=3):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

def demo_caesar():
    msg = "Hello World"
    enc = caesar_encrypt(msg, 5)
    dec = caesar_decrypt(enc, 5)
    print("Caesar ->", "msg:", msg, "| enc:", enc, "| dec:", dec)

def demo_fernet():
    if not CRYPTO_AVAILABLE:
        print("Fernet demo skipped (cryptography not installed).")
        return
    key = Fernet.generate_key()
    cipher = Fernet(key)
    msg = b"Secret Data"
    token = cipher.encrypt(msg)
    plain = cipher.decrypt(token)
    print("Fernet ->", "key:", key, "| token:", token, "| plain:", plain)

if __name__ == "__main__":
    demo_caesar()
    demo_fernet()
