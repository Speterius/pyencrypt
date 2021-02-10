# PyEncrpyt

This repo contains a simple script that allows the user to encrpyt text files using a password derived key.
The same files can later be decrypted using the same password.

## Setup

1) Clone the repository
2) Install dependencies
    
    `python -m venv venv`
    
    `source venv/bin/activate` or `venv\scripts\activate`
    
    `pip install -r requirements.txt`
    
## Usage

Run using: `python pyencrypt`

1) Choose action (Encrpy or Decrypt) using the GUI
2) Enter password for the session
3) Choose file
4) If the password was correct -> Save as

## Further todos:

* save `salt` to device 