from cryptography.fernet import Fernet


# key = Fernet.generate_key()
# with open("key.key", "wb") as file:
#     file.write(key)
def encrypt(pw="master"):
    pw = pw.encode()
    with open("key.key", "rb") as file:
        key = file.read()
        f = Fernet(key)
    return f.encrypt(pw)


def decrypt(ep):
    with open("key.key", "rb") as file:
        key = file.read()
        f = Fernet(key)
    return f.decrypt(ep)


# # mp = encrypt()
# with open("mp.key", "rb") as file:
#     e = file.read()
# print(decrypt(e))



