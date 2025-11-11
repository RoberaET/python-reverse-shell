import base64  # Imports base64 for encoding/decoding binary data to text
from itertools import cycle  # Imports cycle to repeat the key indefinitely

ip = "ipv4.address.here"  # Stores the IP address as a string
port = "portnumberhere"  # Stores the port number as a string
key = b"X" * 32  # Creates a 32-byte key filled with 'X' (for XOR encryption)

def _xor_bytes(data_bytes: bytes, key_bytes: bytes) -> bytes:  # Defines private function for XOR
    return bytes(a ^ b for a, b in zip(data_bytes, cycle(key_bytes)))  # XORs data with cycling key

def encrypt(data: str | bytes) -> str:  # Defines encrypt function accepting str or bytes
    data_bytes = data.encode() if isinstance(data, str) else data  # Converts str to bytes if needed
    return base64.b64encode(_xor_bytes(data_bytes, key)).decode()  # XORs, base64-encodes, returns str

def decrypt(encoded: str) -> str:  # Defines decrypt function taking base64 string
    return _xor_bytes(base64.b64decode(encoded), key).decode()  # base64-decodes, XORs back, returns str

if __name__ == "__main__":  # Runs only if script is executed directly
    enc_ip = encrypt(ip)  # Encrypts the IP address
    enc_port = encrypt(port)  # Encrypts the port number
    print("ENCRYPTED_HOST_BASE64 =", enc_ip)  # Prints encrypted IP in base64
    print("ENCRYPTED_PORT_BASE64 =", enc_port)  # Prints encrypted port in base64
    print("DECRYPTED_HOST =", decrypt(enc_ip))  # Decrypts and prints original IP
    print("DECRYPTED_PORT =", decrypt(enc_port))  # Decrypts and prints original port