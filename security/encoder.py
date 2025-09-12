import base64

def encode_password(password):
    encoded = base64.b64encode(password.encode())
    print(encoded)

user_input = input("Enter your password: ")
encode_password(user_input)