Bem-vindo ao projeto Empresa API! Este projeto foi desenvolvido como parte de um exercício para a Dcifre Contabilidade e tem como objetivo criar uma API para gerenciar empresas e suas obrigações acessórias utilizando FastAPI e SQLAlchemy. A aplicação permite realizar operações CRUD (Create, Read, Update, Delete) em empresas e obrigações acessórias, além de fornecer uma interface de documentação automática usando Swagger UI.

empresa_api/
│── .env  # Variáveis de ambiente
│── database.py  # Configuração do banco de dados
│── models.py  # Modelos do banco de dados
│── schemas.py  # Definições dos dados (Pydantic)
│── crud.py  # Funções de manipulação do banco de dados
│── main.py  # Arquivo principal da API
│── requirements.txt  # Dependências
│── README.md  # Documentação
│── venv/  # Ambiente virtual
│── test_main.py  # Testes

Variáveis de Ambiente:
DB_NAME=empresas
DB_USER=postgres
DB_PASSWORD=1828
DB_HOST=localhost
DB_PORT=5432

Rodar o Servidor:
uvicorn main:app --reload

Acessar a Documentação da API:
http://127.0.0.1:8000/docs


Funcionalidades Principais
Gerenciamento de Empresas:
Criar uma nova empresa.
Listar todas as empresas.
Obter detalhes de uma empresa específica.
Atualizar informações de uma empresa.
Excluir uma empresa.

Gerenciamento de Obrigações Acessórias:
Criar uma nova obrigação acessória.
Listar todas as obrigações acessórias de uma empresa.
Obter detalhes de uma obrigação acessória específica.
Atualizar informações de uma obrigação acessória.
Excluir uma obrigação acessória.

Testes:
pytest

Conclusão:
Foi minha primeira vez trabalhando com banco de dados, e confesso que, se tivesse mais tempo, poderia aperfeiçoar este protótipo. Estou começando agora a trabalhar com os modelos solicitados dentro da minha instituição de ensino. No entanto, foi uma experiência incrível e sinto-me contente com o meu resultado. Trabalhei neste código a madrugada toda para conseguir entregá-lo no prazo. Espero que agrade aos examinadores.
