import pymysql.cursors
from contextlib import contextmanager
from sys import exit


@contextmanager
def conecta():
    """
    Funcao conecta com banco de dados
    Banco de dados local, conectado via XAMPP
    """
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='agenda_simples',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conn
    finally:
        conn.close()


def exibe_menu():
    conecta()
    print('----MENU----'
          '\n\t1 - adicionar contato na lista;'
          '\n\t2 - atualizar contato na lista;'
          '\n\t3 - exlcuir contato na lista;'
          '\n\t4 - pesquisar na lista;'
          '\n\t5 - sair')
    operacao = input("digite uma operação: ")
    percorrendo_menu(operacao)


def percorrendo_menu(operacao):
    if operacao == '1':
        adiciona_contato()
    elif operacao == '2':
        atualiza_contato()
    elif operacao == '3':
        deleta_contato()
    elif operacao == '4':
        exibe_contatos()
    elif operacao == '5':
        print('Saindo...')
        exit()
    else:
        print("Operação não reconhecida")


def adiciona_contato():
    """
    Solicita dados para fazer registro no banco de dados
    """
    print('---Adicionar contato---')
    nome = input('\tnome: ')
    sobrenome = input('\tsobrenome: ')
    email = input('\temail: ')
    celular = input('\tcelular: ')

    # adiciona contato no banco
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql_comando = 'INSERT INTO contato (nome_contato, sobrenome_contato, email_contato, celular) VALUES' \
                          '(%s, %s, %s, %s)'
            cursor.execute(sql_comando, (nome, sobrenome, email, celular))
            conexao.commit()
    print('contato adicionado com sucesso')


def exibe_contatos():
    """
    Exibe contatos no terminal
    """
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql_comando = 'SELECT * FROM contato'
            cursor.execute(sql_comando)
            select = cursor.fetchall()

            for linha in select:
                id_contato = linha['id_contato']
                nome_contato = linha['nome_contato']
                sobrenome_contato = linha['sobrenome_contato']
                email_contato = linha['email_contato']
                celular_contato = linha['celular']
                print(f'\tid: {id_contato} - nome: {nome_contato} {sobrenome_contato} - '
                      f'email: {email_contato} - celular: {celular_contato}')


def atualiza_contato():
    """
    Atualiza contato da lista
    """
    print('---Atualizar contato---')
    exibe_contatos()
    id_atualizar = input('id para atualizar: ')
    nome_atualizar = input('nome atualizado: ')
    sobrenome_atualizado = input('sobrenome atualizado: ')
    email_atualizado = input('email atualizado: ')
    celular_atualizado = input('celular atualizado: ')
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql_comando = 'UPDATE contato SET nome_contato=%s, sobrenome_contato=%s, email_contato=%s, ' \
                          'celular=%s WHERE id_contato=%s'
            cursor.execute(sql_comando, (nome_atualizar, sobrenome_atualizado, email_atualizado, celular_atualizado,
                                         int(id_atualizar)))
            conexao.commit()
    print('atualização feita com sucesso')


def deleta_contato():
    """
    Deleta contato desejado da lista
    """
    print('---Deletar contato---')
    exibe_contatos()
    id_atualizar = input('id para deletar: ')
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql_comando = 'DELETE FROM contato WHERE id_contato=%s'
            cursor.execute(sql_comando, (int(id_atualizar),))
            conexao.commit()
    print('Contato deletado com sucesso.')


if __name__ == '__main__':
    try:
        while True:
            exibe_menu()

    except Exception as e:
        print(f'{e}')
