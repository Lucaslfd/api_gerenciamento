import sqlite3


# Função para criar a tabela 'clientes' se ainda não existir
def criar_tabelas():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('''
                   
    CREATE TABLE clientes (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        nome            TEXT    NOT NULL,
        cpf             TEXT    NOT NULL,
        email           TEXT    NOT NULL,
        telefone        TEXT,
        data_nascimento DATE,
        endereco_id     INTEGER REFERENCES endereco (id),
        FOREIGN KEY (
            endereco_id
        )
        REFERENCES endereco (id) 
)
''')



    conn.commit()
    conn.close()
    


def criar_tabelas_2():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE endereco (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cep TEXT NOT NULL,
            logradouro TEXT NOT NULL,
            complemento TEXT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    ''')

    

    conn.commit()
    conn.close()