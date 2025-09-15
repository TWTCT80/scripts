import base64

def decode_password(password):
    base64_bytes = base64.b64decode(password)
    message_bytes = base64_bytes.decode()
    print(message_bytes)

user_input = input("Enter your encoded string: ")
decode_password(user_input)

# b'aGVqc2Fu'