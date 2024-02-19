from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class Cryptography:

    def __init__(self, private_key=None, public_key=None) -> None:
        self.private_key = private_key
        self.public_key = public_key

    def generate_key_pair(self, mode='set'):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        self.private_key = private_pem
        self.public_key = public_pem
        
        if mode == 'set':
            print('Keys have been set')
        else:
            return self.private_key, self.public_key

    def encrypt_message(self, message):
        _public_key = serialization.load_pem_public_key(self.public_key, backend=default_backend())
        encrypted_message = _public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        _private_key = serialization.load_pem_private_key(self.private_key, password=None, backend=default_backend())
        decrypted_message = _private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message.decode('utf-8')

    def check_key_pair_truth(self):
        private_key_obj = serialization.load_pem_private_key(self.private_key, password=None, backend=default_backend())
        public_key_obj = serialization.load_pem_public_key(self.public_key, backend=default_backend())

        # Sign a dummy message with the private key
        message = b"dummy_message_for_key_verification"
        signature = private_key_obj.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Verify the signature with the public key
        try:
            public_key_obj.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False

if __name__ == '__main__':
    c = Cryptography()
    c.generate_key_pair()
    # Encrypt and Decrypt a message
    c.public_key
    message = "Hello, this is a secret message!"
    encrypted_message = c.encrypt_message(message)
    encrypted_message
    decrypted_message = c.decrypt_message(encrypted_message)
    decrypted_message

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

    c.check_key_pair_truth()