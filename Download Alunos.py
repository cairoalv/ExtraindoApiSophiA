import requests


chav2 = ''
with open('token.txt', 'r') as file:
    chav2 += file.read()

    print (chav2)

headers = {
    'token': chav2
}

url = requests.get("https://portal.sophia.com.br/SophiAWebAPI/3055/api/v1/Alunos", headers=headers).json()

response_dados = url

CodAluno = []
NomeAluno = []
EmailAluno = []
TurmaAluno = []

for aluno in url:
    CodAluno.append(aluno['codigoExterno'])
    NomeAluno.append(aluno['nome'])
    EmailAluno.append(aluno['email'])


