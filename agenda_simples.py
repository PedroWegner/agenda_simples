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


if __name__ == '__main__':
    try:
        conecta()
        print('Conexão sucesso')
    except Exception as e:
        print(f'Não possível conectar ao banco. Erro: {e}')