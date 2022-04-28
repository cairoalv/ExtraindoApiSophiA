import json
import requests
import pandas as pd
import openpyxl


chav2 = ''
with open('token.txt', 'r') as file:
    chav2 += file.read()

    print (chav2)

headers = {
    'token': chav2
}

url = requests.get("https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos", headers=headers).json()

CodAluno = []
NomeAluno = []
EmailAluno = []
TurmaAluno = []


for aluno in url:
    CodAluno.append(aluno['codigoExterno'])
    NomeAluno.append(aluno['nome'])
    EmailAluno.append(aluno['email'])
    TurmaAluno.append(aluno['turmas'])

print(TurmaAluno)

dados = pd.DataFrame(list(zip(CodAluno, NomeAluno, EmailAluno)), columns=['CodigoExterno','Nome','Email'])

dados.to_excel('Alunos.xlsx', index = False)