**Mulher.com - Sistema de Gerenciamento de Clientes**
=====================================================

**Resumo**
-----------

O sistema de gerenciamento de clientes da Mulher.com tem como objetivo armazenar e gerenciar os dados pessoais dos clientes da loja de bolsas femininas. O sistema deve ser capaz de armazenar informações como nome, sobrenome, data de nascimento, sexo, endereço, cidade, estado e e-mails dos clientes.

**Requisitos Funcionais**
-------------------------

### RF001 - Cadastro de Clientes

* O sistema deve permitir o cadastro de novos clientes com os seguintes dados:
	+ Nome
	+ Sobrenome
	+ Data de nascimento
	+ Sexo
	+ Endereço (rua, número, bairro, cidade, estado)
	+ E-mails (pode ter múltiplos e-mails)
* O sistema deve validar os dados de entrada para garantir a consistência e integridade dos dados.

### RF002 - Consulta de Clientes

* O sistema deve permitir a consulta de clientes cadastrados com base nos seguintes critérios:
	+ Nome
	+ Sobrenome
	+ Data de nascimento
	+ Sexo
	+ Endereço (rua, número, bairro, cidade, estado)
	+ E-mails
* O sistema deve retornar uma lista de clientes que atendem aos critérios de busca.

### RF003 - Edição de Clientes

* O sistema deve permitir a edição dos dados de clientes cadastrados.
* O sistema deve validar os dados de entrada para garantir a consistência e integridade dos dados.

### RF004 - Exclusão de Clientes

* O sistema deve permitir a exclusão de clientes cadastrados.
* O sistema deve solicitar confirmação antes de excluir um cliente.

**Requisitos Não Funcionais**
---------------------------

### RNF001 - Performance

* O sistema deve ser capaz de lidar com um volume de até 10.000 clientes cadastrados.
* O sistema deve ter um tempo de resposta de no máximo 2 segundos para cada operação.

### RNF002 - Segurança

* O sistema deve garantir a integridade e confidencialidade dos dados dos clientes.
* O sistema deve utilizar criptografia para proteger os dados sensíveis.

### RNF003 - Usabilidade

* O sistema deve ter uma interface de usuário fácil de usar e intuitiva.
* O sistema deve fornecer mensagens de erro claras e precisas em caso de erro.

**Modelo de Dados**
-----------------

### Entidades

* **Pessoa**
	+ id (chave primária)
	+ nome
	+ sobrenome
	+ dataNascimento
	+ sexo
* **Endereco**
	+ id (chave primária)
	+ rua
	+ numero
	+ bairro
	+ cidade (chave estrangeira para Cidade)
	+ estado (chave estrangeira para Estado)
* **Cidade**
	+ id (chave primária)
	+ nome
* **Estado**
	+ id (chave primária)
	+ nome
* **Email**
	+ id (chave primária)
	+ enderecoEmail
	+ pessoa (chave estrangeira para Pessoa)

**Relacionamentos**

* Uma pessoa tem um endereço (Pessoa 1--1 Endereco)
* Um endereço pertence a uma pessoa (Endereco 1--1 Pessoa)
* Uma pessoa tem muitos e-mails (Pessoa 1--* Email)
* Um e-mail pertence a uma pessoa (Email *--1 Pessoa)
* Uma cidade pertence a um estado (Cidade 1--1 Estado)
* Um estado tem muitas cidades (Estado 1--* Cidade)

**Tecnologias**
--------------

* Banco de dados: MySQL
* Linguagem de programação: Java
* Framework: Spring Boot
* Interface de usuário: HTML, CSS, JavaScript

**Conclusão**
----------

O sistema de gerenciamento de clientes da Mulher.com deve ser capaz de armazenar e gerenciar os dados pessoais dos clientes da loja de bolsas femininas. O sistema deve ser fácil de usar, seguro e escalável para atender às necessidades da loja.
