## Instalação
Instruções para instalar e rodar o projeto localmente. Por exemplo:
Clone o repositório: git clone https://github.com/Lucaslfd/api_gerenciamento_leads.git
Instale as dependências: pip install -r requirements.txt
Rode o projeto: python app.py

## 1. Importação de Bibliotecas
Flask: Utilizado para criar a aplicação web.
jsonify, request: Facilitam a manipulação de dados JSON.
databaseArc: Módulo personalizado para criar tabelas no banco de dados.
sqlite3: Integração com o banco de dados SQLite.
CORS: Lidar com problemas de política de mesma origem (Cross-Origin Resource Sharing).

# 2. Rotas

## 3.1. Rota Principal

@app.route('/')
def hello_world():
    return 'Hello World!'
'/': Rota principal que retorna a mensagem "Hello World!".


## 3.2. Rota para Criar Tabelas no Banco de Dados
@app.route('/criartabelas')
def hello_world2():
    """
    Função para criar tabelas no banco de dados
    """
    criar_tabelas_2()
    criar_tabelas()
    return "Sucesso, tabelas criadas!"
'/criartabelas': Rota para criar tabelas no banco de dados utilizando funções definidas no módulo databaseArc.


## 3.3. Rota para Listar Clientes

@app.route('/cliente', methods=['GET'])
def listar_clientes():
    """
    Função para listar clientes no banco de dados
    """
    # ...
'/cliente': Rota para listar todos os clientes no banco de dados.


## 3.4. Rota para Listar Endereços

@app.route('/endereco', methods=['GET'])
def listar_enderecos():
    """
    Função para listar endereços no banco de dados
    """
    # ...
'/endereco': Rota para listar todos os endereços no banco de dados.


## 3.5. Rota para Obter Endereço por ID

@app.route('/endereco/id/<int:id>', methods=['GET'])
def obter_endereco_por_id(id):
    # ...
'/endereco/id/int:id': Rota para obter informações de um endereço específico com base no ID.


## 3.6. Rota para Cadastrar Cliente

@app.route('/cliente', methods=['POST'])
def cadastrar_cliente():
    """
    Função para cadastrar clientes no banco de dados
    """
    # ...
'/cliente': Rota para cadastrar um novo cliente no banco de dados.


## 3.7. Rota para Cadastrar Endereço

@app.route('/endereco', methods=['POST'])
def cadastrar_endereco():
    """
    Função para cadastrar endereços no banco de dados
    """
    # ...
'/endereco': Rota para cadastrar um novo endereço no banco de dados.


## 3.8. Rota para Editar Cliente

@app.route('/cliente/<int:id>', methods=['PUT'])
def editar_cliente(id):
    """
    Função para editar clientes no banco de dados
    """
    # ...
'/cliente/int:id': Rota para editar informações de um cliente existente com base no ID.


## 3.9. Rota para Editar Endereço

@app.route('/endereco/<int:id>', methods=['PUT'])
def editar_endereco(id):
    """
    Função para editar endereços no banco de dados
    """
    # ...
'/endereco/int:id': Rota para editar informações de um endereço existente com base no ID.


## 3.10. Rota para Excluir Cliente

@app.route('/cliente/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    """
    Função para excluir clientes no banco de dados
    """
    # ...
'/cliente/int:id': Rota para excluir um cliente com base no ID fornecido.


## 3.11. Rota para Excluir Endereço

@app.route('/endereco/<int:id>', methods=['DELETE'])
def excluir_endereco(id):
    """
    Função para excluir endereços no banco de dados
    """
    # ...
'/endereco/int:id': Rota para excluir um endereço com base no ID fornecido.


## 3.12. Rota para Obter Cliente por ID

@app.route('/cliente/<int:id>', methods=['GET'])
def obter_cliente_por_id(id):
    # ...
'/cliente/int:id': Rota para obter informações de um cliente específico com base no ID.


## 3.13. Rota para Obter Endereço por CEP

@app.route('/endereco/cep/<string:cep>', methods=['GET'])
def obter_endereco_por_cep(cep):
    # ...
'/endereco/cep/string:cep': Rota para obter informações de um endereço específico com base no CEP.