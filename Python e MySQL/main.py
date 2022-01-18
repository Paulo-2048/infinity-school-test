from datetime import datetime

from database import Connection
from userDb import UserConection
from user import User


db = Connection()
db.connect()

userDb = UserConection(db.con)

print('Bem Vindo a Aplicação')
ch = int(input('''
Menu de Opções

1 - Cadastrar novo usuário
2 - Acesso administrativo\n'''))

if ch == 1:
    name = input('Insira o Nome: ')
    email = input('Insira o Email: ')
    senha = input('Insira a Senha: ')
    people = User(name, email, senha, datetime.now())
    if userDb.insertUser(people):
        print('Usuário cadastrado com sucesso!')
    else:
        print('Algo deu errado, tente novamente.')

if ch == 2:
    verEmail = input('Insira o email: ')
    verSenha = input('Insira a senha: ')
    while True:
        res = (userDb.ver_acess(verEmail, verSenha))
        if res and res[0][5] == 1:
            print(f'Bem vindo {res[0][1]}')
            ch = int(input('''
            Menu Administrativo
            1 - Listar Usuários
            2 - Editar Usuário
            3 - Remover Usuário\n'''))
            if ch == 1:
                listUser = userDb.listing()

                for i in listUser:
                    print(f'''
                IdCode: {i[0]}
                Nome: {i[1]}
                Email: {i[2]}
                Senha: ****
                Data e Hora: {i[4]}
                Acesso: {i[5]}
                    ''')
            elif ch == 2:
                idCode = int(input('Insira o Código Id do Usuário: '))
                col = int(input('''
                Alterações Possivéis:
                1 - Nome
                2 - Email
                3 - Acesso\n'''))
                val = input('Insira o novo valor: ')
                if userDb.update_data(col, val, idCode):
                    print('Úsuario Atualizado')
                else:
                    print('Algo deu errado!')
            elif ch == 3:
                idCode = int(input('Insira o Código Id do Usuário: '))
                if userDb.delete_data(idCode):
                    print('Usuário Deletado com Sucesso')
                else:
                    print('Algo Deu errado!')

            ret = input('Deseja voltar ao menu administrativo? (s/n): ').lower()
            if ret == 's':
                pass
            else:
                break
        else:
            print('Administrador não Cadastrado ou sem Acesso')
            break




