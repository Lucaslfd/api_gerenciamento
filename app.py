from flask import Flask, jsonify, request
from databaseArc import criar_tabelas, criar_tabelas_2
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/criartabelas')
def hello_world2():
    """
    Função para criar tabelas no banco de dados
    """
    criar_tabelas_2()
    criar_tabelas()
    return "Sucesso, tabelas criadas!"

# Endpoint para listar todos os clientes
@app.route('/cliente', methods=['GET'])
def listar_clientes():
    """
    Função para listar clientes no banco de dados
    """
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    conn.close()

    return jsonify(clientes)

@app.route('/endereco', methods=['GET'])
def listar_enderecos():
    """
    Função para listar enderecos no banco de dados
    """
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM endereco')
    enderecos = cursor.fetchall()

    conn.close()

    return jsonify(enderecos)


@app.route('/endereco/id/<int:id>', methods=['GET'])
def obter_endereco_por_id(id):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # Buscar endereco pelo ID
    cursor.execute('SELECT * FROM endereco WHERE id = ?', (id,))
    endereco = cursor.fetchone()

    conn.close()
    print(endereco)
    if endereco:
        # Se o Endereco for encontrado, retorna suas informações
        return jsonify({
            "id": endereco[0],
            "cep": endereco[1],
            "logradouro": endereco[2],
            "complemento": endereco[3],
            "bairro": endereco[4],
            "cidade": endereco[5],
            "estado": endereco[6]
        })

        
    
     # Se o Endereco não for encontrado, retorna uma mensagem de erro
    else:
        return jsonify({"erro": "Endereco não encontrado"}), 404



# Endpoint para cadastrar um novo cliente
@app.route('/cliente', methods=['POST'])
def cadastrar_cliente():
    """
    Função para cadastrar clientes no banco de dados
    """
    novo_cliente = request.get_json()

    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO clientes (nome, cpf, email, telefone, data_nascimento, endereco_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        novo_cliente['nome'],
        novo_cliente['cpf'],
        novo_cliente['email'],
        novo_cliente.get('telefone'),  # Usando get para lidar com o caso de telefone opcional
        novo_cliente.get('data_nascimento'),  # Usando get para lidar com o caso de data_nascimento opcional
        novo_cliente.get('endereco_id'),  # Usando get para lidar com o caso de endereco_id opcional
    ))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"})


@app.route('/endereco', methods=['POST'])
def cadastrar_endereco():
    """
    Função para cadastrar endereco no banco de dados
    """
    novo_endereco = request.get_json()

    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO endereco (cep, logradouro, complemento, bairro, cidade, estado)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        novo_endereco['cep'],
        novo_endereco['logradouro'],
        novo_endereco['complemento'],
        novo_endereco.get('bairro'),  # Usando get para lidar com o caso de telefone opcional
        novo_endereco.get('cidade'),  # Usando get para lidar com o caso de data_nascimento opcional
        novo_endereco.get('estado'),  # Usando get para lidar com o caso de endereco_id opcional
    ))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"})


# Endpoint para editar um cliente existente
@app.route('/cliente/<int:id>', methods=['PUT'])
def editar_cliente(id):
    """
    Função para editar clientes no banco de dados
    """
    dados_atualizados = request.get_json()

    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE clientes
        SET nome=?, cpf=?, email=?, telefone=?, data_nascimento=?, endereco_id=?
        WHERE id=?
    ''', (
        dados_atualizados['nome'],
        dados_atualizados['cpf'],
        dados_atualizados['email'],
        dados_atualizados.get('telefone'),
        dados_atualizados.get('data_nascimento'),
        dados_atualizados.get('endereco_id'),
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Cliente atualizado com sucesso!"})


@app.route('/endereco/<int:id>', methods=['PUT'])
def editar_endereco(id):
    """
    Função para editar endereco no banco de dados
    """
    dados_atualizados = request.get_json()

    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE endereco
        SET cep=?, logradouro=?, complemento=?, bairro=?, cidade=?, estado=?
        WHERE id=?
    ''', (
        dados_atualizados['cep'],
        dados_atualizados['logradouro'],
        dados_atualizados['complemento'],
        dados_atualizados.get('bairro'),
        dados_atualizados.get('cidade'),
        dados_atualizados.get('estado'),
        id
    ))

    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Endereco atualizado com sucesso!"})

# Endpoint para excluir um cliente com base no ID fornecido
@app.route('/cliente/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    """
    Função para excluir clientes no banco de dados
    """
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM clientes WHERE id=?', (id,))
    conn.commit()

    conn.close()

    return jsonify({"mensagem": "Cliente excluído com sucesso!"})


@app.route('/endereco/<int:id>', methods=['DELETE'])
def excluir_endereco(id):
    """
    Função para excluir endereco no banco de dados
    """
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM endereco WHERE id=?', (id,))
    conn.commit()

    conn.close()

    return jsonify({"mensagem": "Endereco excluído com sucesso!"})



@app.route('/cliente/<int:id>', methods=['GET'])
def obter_cliente_por_id(id):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # Buscar cliente pelo ID
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    cliente = cursor.fetchone()

    conn.close()

    if cliente:
        # Se o cliente for encontrado, retorna suas informações
        return jsonify({
            "id": cliente[0],
            "nome": cliente[1],
            "cpf": cliente[2],
            "email": cliente[3],
            "telefone": cliente[4],
            "data_nascimento": cliente[5],
            "endereco_id": cliente[6]
        })
    else:
        # Se o Cliuente não for encontrado, retorna uma mensagem de erro
        return jsonify({"erro": "Cliente não encontrado"}), 404
    



    
@app.route('/endereco/cep/<string:cep>', methods=['GET'])
def obter_endereco_por_cep(cep):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # Buscar endereco pelo ID
    cursor.execute('SELECT * FROM endereco WHERE cep = ? LIMIT 1', (cep,))
    endereco = cursor.fetchone()

    conn.close()

    if endereco:
        # Se o Endereco for encontrado, retorna suas informações
        return jsonify({
            "id": endereco[0],
            "nome": endereco[1],
            "cpf": endereco[2],
            "email": endereco[3],
            "telefone": endereco[4],
            "data_nascimento": endereco[5],
            "endereco_id": endereco[6]
        })
    
     # Se o Endereco não for encontrado, retorna uma mensagem de erro
    else:
        return jsonify({"erro": "Endereco não encontrado"}), 404




if __name__ == '__main__':
    app.run()


