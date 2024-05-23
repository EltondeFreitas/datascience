**Mulher.com - Sistema de Gerenciamento de Clientes**
======================================================

**Documento de Especificação de Requisitos**
------------------------------------------

**Resumo**
-----------

O sistema de gerenciamento de clientes da Mulher.com tem como objetivo armazenar e gerenciar os dados pessoais dos clientes da loja de bolsas femininas. O sistema deve ser capaz de armazenar informações como nome, sobrenome, data de nascimento, CPF, endereço, cidade, estado e e-mails dos clientes.

**Requisitos Funcionais**
-------------------------

### 1. Cadastro de Clientes

* O sistema deve permitir o cadastro de novos clientes com os seguintes dados:
	+ Nome
	+ Sobrenome
	+ Data de nascimento
	+ CPF
	+ Endereço (rua, número, complemento, bairro, CEP)
	+ Cidade
	+ Estado
	+ E-mail (pode ter vários)
* O sistema deve validar os dados de entrada para garantir a consistência e integridade dos dados.

### 2. Consulta de Clientes

* O sistema deve permitir a consulta de clientes cadastrados com base nos seguintes critérios:
	+ Nome
	+ Sobrenome
	+ CPF
	+ E-mail
* O sistema deve retornar os dados do cliente, incluindo endereço, cidade e estado.

### 3. Edição de Clientes

* O sistema deve permitir a edição dos dados de clientes cadastrados.
* O sistema deve validar os dados de entrada para garantir a consistência e integridade dos dados.

### 4. Exclusão de Clientes

* O sistema deve permitir a exclusão de clientes cadastrados.
* O sistema deve solicitar confirmação antes de excluir um cliente.

**Requisitos Não Funcionais**
---------------------------

### 1. Performance

* O sistema deve ser capaz de lidar com um volume de dados razoável sem comprometer a performance.
* O sistema deve ser capaz de realizar operações de cadastro, consulta, edição e exclusão de clientes em um tempo razoável.

### 2. Segurança

* O sistema deve garantir a segurança dos dados dos clientes, protegendo contra acessos não autorizados e perda de dados.
* O sistema deve utilizar criptografia para proteger os dados sensíveis, como CPF e e-mails.

### 3. Usabilidade

* O sistema deve ser fácil de usar e intuitivo para os usuários.
* O sistema deve fornecer mensagens de erro claras e concisas em caso de problemas.

**Modelo de Dados**
-----------------

### Entidades

* **Pessoa**
	+ id (chave primária)
	+ nome
	+ sobrenome
	+ dataNascimento
	+ cpf
* **Endereço**
	+ id (chave primária)
	+ rua
	+ número
	+ complemento
	+ bairro
	+ cep
	+ pessoa_id (chave estrangeira que referencia a entidade Pessoa)
* **Cidade**
	+ id (chave primária)
	+ nome
	+ estado_id (chave estrangeira que referencia a entidade Estado)
* **Estado**
	+ id (chave primária)
	+ nome
	+ sigla
* **E-mail**
	+ id (chave primária)
	+ endereco
	+ pessoa_id (chave estrangeira que referencia a entidade Pessoa)

### Relacionamentos

* Uma pessoa tem um endereço (one-to-one)
* Uma pessoa pode ter vários e-mails (one-to-many)
* Um endereço está localizado em uma cidade (many-to-one)
* Uma cidade está localizada em um estado (many-to-one)

**Tecnologias**
--------------

* Banco de dados: MySQL
* Linguagem de programação: Java
* Framework: Spring Boot
* Interface de usuário: HTML, CSS, JavaScript

**Conclusão**
----------

O sistema de gerenciamento de clientes da Mulher.com deve ser capaz de armazenar e gerenciar os dados pessoais dos clientes da loja de bolsas femininas. O sistema deve ser seguro, escalável e fácil de usar. Este documento de especificação de requisitos fornece uma visão geral das funcionalidades e requisitos do sistema.
