import json # Importa biblioteca json
import os # Importa biblioteca os
import time # Importa biblioteca time
from datetime import datetime # Importa biblioteca datetime

############ DELETE OLDER THAN X ############
with open('config.json') as json_file: # Abre arquivo config.json
    data = json.load(json_file) # Carrega arquivo config.json

daysToDelete = int(data['daysToDelete']) # Dias para excluir
directory = data['directory'] # Diretório

excludeDirs  = set(data['excludeDirs']) # Pastas para excluir

current_time = time.time() # Tempo atual

while True: # Loop infinito
    for dirpath, dirs, filenames in os.walk(directory): # Percorre diretório

        dirs[:] = [d for d in dirs if d not in excludeDirs] # dirs[:] = [d for d in dirs if d not in excludeDirs] # Exclui pastas
        
        for f in filenames: # Exclui arquivos
            fileWithPath = os.path.abspath(os.path.join(dirpath, f)) # Caminho completo do arquivo
            creation_time = os.path.getctime(fileWithPath) # Data de criação do arquivo
            if ((current_time - creation_time) // (24 * 3600) >= daysToDelete) and ((current_time - creation_time) // (24 * 3600) < 180): # Exclui arquivos com mais de 180 dias
                os.unlink(fileWithPath) # Remove arquivo
                print('{} removed'.format(fileWithPath)) # Exibe arquivo removido
                with open('removeds.txt', 'a+', encoding='utf-8') as f: # Grava arquivo removido
                    f.write('\n' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ' - ' + fileWithPath + ' | CRDATE: ' + datetime.fromtimestamp(creation_time).strftime('%d-%m-%Y %H:%M:%S') + ' removed') 
    # Grava arquivo removido ^
            else: # Exibe arquivo não removido
                print('{} not removed'.format(fileWithPath)) # Exibe arquivo não removido
    # Informar que nao possui arquivos para excluir no tempo especificado e grava arquivo
        
        if not dirs and not filenames: # Se não existir pastas e arquivos
            print(f'Não existem arquivos para remover com mais de {daysToDelete} dias no diretorio {dirpath}') # Exibe mensagem
            with open('removeds.txt', 'a+', encoding='utf-8') as f: # Grava arquivo removido
                f.write('\n' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + ' - Não existem arquivos para remover com mais de ' + str(daysToDelete) + ' dias no diretorio ' + dirpath) # Grava arquivo removido
    time.sleep(1800) # Tempo para executar novamente (1800 = 30 minutos)
# Função para excluir pastas
""" __summary:
Função para excluir pastas
Args:
    dirpath (string): Diretório atual

    dirs (list): Lista de diretórios

    filenames (list): Lista de arquivos

Returns:
    list: Lista de diretórios excluídos
"""

# Precionar enter para sair
input('Pressione <enter> para sair...')