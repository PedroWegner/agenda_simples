import pymysql.cursors
from contextlib import contextmanager


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


if __name__ == '__main__':
    try:
        conecta()
        print('Conexão sucesso')

        # crud simples
        # adiciona contato no banco
        # with conecta() as conexao:
        #     with conexao.cursor() as cursor:
        #         sql_comando = 'INSERT INTO contato (nome_contato, sobrenome_contato, email_contato, celular) VALUES' \
        #                       '(%s, %s, %s, %s)'
        #         cursor.execute(sql_comando, ('Pedro', 'Wegner', 'pedrowegner', '41 99672-2273'))
        #         conexao.commit()

        # le contato no banco
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql_comando = 'SELECT * FROM contato'
                cursor.execute(sql_comando)
                select = cursor.fetchall()

                for linha in select:
                    print(linha)

        #
        # # atualiza contato no banco
        # with conecta() as conexao:
        #     with conexao.cursor() as cursor:
        #         sql_comando = ''
        #         cursor.execute(sql_comando)
        #         conexao.commit()
        #
        # # exclui contato no banco
        # with conecta() as conexao:
        #     with conexao.cursor() as cursor:
        #         sql_comando = ''
        #         cursor.execute(sql_comando)
        #         conexao.commit()

    except Exception as e:
        print(f'{e}')
