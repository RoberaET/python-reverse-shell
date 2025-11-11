# Python Reverse Shell

## Description
Python reverse shell with XOR encryption for educational purposes only. Experimental - may not work reliably in all environments.

## License
MIT License

## Features
- XOR encryption for host/port
- Hidden console on Windows
- Daemon thread for persistence
- Basic command execution

## Usage
1. Encrypt host/port using the encryption script.
2. Replace placeholders in code.
3. Run `pyinstaller --onefile --noconsole reverse_shell.py` to build EXE.
4. EXE is not detected by most AVs (tested on VirusTotal).

## Disclaimer
For educational use only. Author not responsible for misuse.
<img width="1917" height="838" alt="image" src="https://github.com/user-attachments/assets/1f90bf5c-7a21-47e5-b76f-ad79660c0be5" />


## Building EXE
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole reverse_shell.py
```
