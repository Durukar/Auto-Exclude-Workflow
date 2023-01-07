# Auto Exclude - PY 🗑️
Este é um script que busca por arquivos e pastas em um determinado diretório e, caso o tempo de criação do arquivo seja maior que um determinado número de dias especificado em um arquivo de configuração, o arquivo é excluído. O script também exclui pastas especificadas em um arquivo de configuração.
<br>
# Requisitos 📋
Python 3.6 ou superior 🐍<br>
Módulos json, os e time 📜
<br>
# Uso 💻
Adicione o arquivo de configuração config.json na mesma pasta do script, seguindo o seguinte formato:
```
{
    "daysToDelete": 30,
    "directory": "/caminho/para/diretorio",
    "excludeDirs": ["pasta1", "pasta2"]
}
```
Onde daysToDelete é o número de dias para exclusão dos arquivos, directory é o caminho para o diretório onde os arquivos serão excluídos e excludeDirs é uma lista de pastas a serem excluídas.

Execute o script com o comando:
```
python autoexclude.py
```
O script irá gerar um arquivo chamado removeds.txt, onde serão registrados os arquivos excluídos, incluindo a data e hora da exclusão e a data de criação do arquivo.

Para sair do script, basta pressionar enter.
<br>
# Observações ⚠️
O script é executado em loop infinito a cada 30 minutos.
Arquivos com mais de 180 dias de criação não serão excluídos.
<br>
# Licença 📃
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
<br>
<br>
# EN
<br>
<br>
# Auto Exclude - PY 🗑️
This is a script that searches for files and directories in a specified directory and, if the file creation time is greater than a specified number of days specified in a configuration file, the file is deleted. The script also deletes directories specified in a configuration file.
<br>
# Requirements 📋
Python 3.6 or higher 🐍
json, os and time modules 📜
<br>
# Usage 💻
Add the configuration file config.json in the same folder as the script, following the following format:
```
{
    "daysToDelete": 30,
    "directory": "/path/to/directory",
    "excludeDirs": ["folder1", "folder2"]
}
```
Where daysToDelete is the number of days for file deletion, directory is the path to the directory where the files will be deleted and excludeDirs is a list of folders to be deleted.

Run the script with the command:
```
python delete_files_and_dirs.py
```
The script will generate a file called removeds.txt, where deleted files will be recorded, including the deletion date and time and the file creation date.

To exit the script, just press enter.
<br>
# Notes ⚠️
The script runs in an infinite loop every 30 minutes.
Files with more than 180 days of creation will not be deleted.
<br>
# License 📃
This project is licensed under the MIT license. See the LICENSE file for more details.
