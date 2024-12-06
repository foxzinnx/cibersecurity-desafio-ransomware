import os
import pyaes
import logging


logging.basicConfig(filename='decryption.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def decrypt_file(file_name, key):
    try:
        
        if not os.path.isfile(file_name):
            logging.error(f"Arquivo criptografado {file_name} não encontrado.")
            return False

        
        with open(file_name, "rb") as file:
            file_data = file.read()

        
        aes = pyaes.AESModeOfOperationCTR(key)

        
        decrypted_data = aes.decrypt(file_data)

        
        os.remove(file_name)
        logging.info(f"Arquivo criptografado {file_name} removido com sucesso.")

        
        new_file_name = file_name.replace(".ransomwaretroll", "")  
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypted_data)
        
        logging.info(f"Arquivo descriptografado salvo como {new_file_name}")
        return True
    
    except Exception as e:
        logging.error(f"Erro durante a descriptografia do arquivo {file_name}: {e}")
        return False


key = b"testeransomwares"


file_name = "teste.txt.ransomwaretroll"


if decrypt_file(file_name, key):
    print(f"O arquivo {file_name} foi descriptografado com sucesso.")
else:
    print(f"Erro ao descriptografar o arquivo {file_name}.")
