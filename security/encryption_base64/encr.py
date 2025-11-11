# Simple script that decodes a base64 string, will add some error handling later on

import base64

def decode_pass(password: str):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"Decoded password: {decode_data}")

def encode_pass(password: str):
    coded_bytes = base64.b64encode(password.encode())
    coded_string = coded_bytes.decode()
    print(f"Encoded passwd: {coded_string}")


choice = 1
while choice != 9:

    choice = int(input("Enter 1 for encoding or enter 2 for decoding (9 to quit): "))

    if choice == 1:
        kod = input("Enter text to code: ")
        encode_pass(kod)
    elif choice == 2:
        encode_string = input("Enter the base64 string: ")
        decode_pass(encode_string)
    
    elif choice == 9:
        print("Bye!")
        break
    else:
        print("Try again")