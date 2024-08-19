import hashlib 

def hash_password(password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return hash_password

password = input('Enter password: ')
hashed_password = hash_password(password)
print('Hashed Password:', hashed_password)
print(len('185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969'))
