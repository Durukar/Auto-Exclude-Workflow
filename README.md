# Exclusão de Arquivos e Pastas 🗑️
Este é um script que busca por arquivos e pastas em um determinado diretório e, caso o tempo de criação do arquivo seja maior que um determinado número de dias especificado em um arquivo de configuração, o arquivo é excluído. O script também exclui pastas especificadas em um arquivo de configuração.
<br>
# Requisitos 📋
Python 3.6 ou superior 🐍
Módulos json, os e time 📜
<br>
# Uso 💻
Adicione o arquivo de configuração config.json na mesma pasta do script, seguindo o seguinte formato:
Copy code
```
{
    "daysToDelete": 30,
    "directory": "/caminho/para/diretorio",
    "excludeDirs": ["pasta1", "pasta2"]
}
```
Onde daysToDelete é o número de dias para exclusão dos arquivos, directory é o caminho para o diretório onde os arquivos serão excluídos e excludeDirs é uma lista de pastas a serem excluídas.

Execute o script com o comando:
Copy code
```python autoexclude.py```
O script irá gerar um arquivo chamado removeds.txt, onde serão registrados os arquivos excluídos, incluindo a data e hora da exclusão e a data de criação do arquivo.

Para sair do script, basta pressionar enter.
<br>
# Observações ⚠️
O script é executado em loop infinito a cada 30 minutos.
Arquivos com mais de 180 dias de criação não serão excluídos.
<br>
# Licença 📃
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
