# Desafio Ransomware

Este repositório contém um exemplo simples de um processo de criptografia e descriptografia, simulando o comportamento de um ransomware. 
O processo envolve dois scripts Python: `encrypter.py` (criptografar) e `decrypter.py` (descriptografar). 

1. **Estrutura Inicial**: A estrutura do diretório antes de qualquer operação: ``` decrypter.py  encrypter.py  myenv  README.md  teste.txt ```
2. **Criptografando um Arquivo**: Execute o script `encrypter.py` para criptografar um arquivo. Exemplo: ```bash $ python encrypter.py ``` Saída: ``` Arquivo criptografado como teste.txt.ransomwaretroll ``` Isso cria um arquivo criptografado chamado `teste.txt.ransomwaretroll`.
3. **Editando o Arquivo Criptografado**: Você pode editar o arquivo criptografado com qualquer editor de texto. Exemplo usando o `nano`: ```bash $ nano teste.txt.ransomwaretroll ```
4. **Descriptografando o Arquivo**: Execute o script `decrypter.py` para restaurar o arquivo original: ```bash $ python decrypter.py ``` Saída: ``` Arquivo descriptografado como teste.txt ``` O arquivo original (`teste.txt`) será restaurado.
5. **Estrutura Final**: Após a descriptografia, a estrutura do diretório será: ``` decrypter.py  encrypter.py  myenv  README.md  teste.txt ``` ## Requisitos Para rodar os scripts, é necessário ter um ambiente Python configurado. Você pode configurar um ambiente virtual da seguinte forma:
                     1. Crie o ambiente virtual: ```bash python -m venv myenv ```
                     2. Ative o ambiente: - No Windows: ```bash myenv\Scripts\activate ``` - No Linux/macOS: ```bash source myenv/bin/activate ```
                     3. Instale as dependências necessárias (caso existam) com: ```bash pip install -r requirements.txt ```


## Como Funciona - O script `encrypter.py` aplica uma criptografia simples ao arquivo especificado. - O script `decrypter.py` reverte a criptografia, restaurando o arquivo original.

## Aviso Este é um exemplo de criptografia e descriptografia com fins educacionais. Não é um software de produção e deve ser utilizado com cuidado.

![desafio-1](https://github.com/user-attachments/assets/ba6a98c6-1be5-4a73-9f78-8445346c7227)
![desafio-2](https://github.com/user-attachments/assets/1df6afb0-804f-4423-a095-4467859d4acd)
![desafio-3](https://github.com/user-attachments/assets/11f7679e-da86-4273-93be-0921502452ba)
![desafio-4](https://github.com/user-attachments/assets/954dccbf-e3fd-4e3b-bf59-5cd913bc5aa5)




