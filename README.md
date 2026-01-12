## 📚 API Sistema Escolar

Projeto de estudo voltado ao **desenvolvimento Backend** com **Python e Flask**, com o objetivo de praticar a criação de **APIs REST**, organização de código e boas práticas de arquitetura.

A API é responsável pelo gerenciamento das entidades **Aluno** e **Professor**, implementando operações completas de **CRUD (Create, Read, Update e Delete)**.

---

## 🚀 Tecnologias Utilizadas

* Python
* Flask
* Flask Blueprint
* JSON (jsonify)
* Git & GitHub

---

## 🧱 Arquitetura do Projeto

O projeto segue uma organização inspirada no padrão **MVC**, separando responsabilidades entre:

* **Controller**: responsável por receber as requisições HTTP, processar as ações e retornar respostas em JSON
* **Model**: responsável pela lógica de dados e estrutura das entidades

Essa separação torna o código mais organizado, legível e fácil de manter.

---

## 📌 Funcionalidades

### 👨‍🎓 Alunos

* Criar aluno
* Listar alunos
* Atualizar aluno
* Deletar aluno

### 👨‍🏫 Professores

* Criar professor
* Listar professores
* Atualizar professor
* Deletar professor

Todas as funcionalidades seguem os princípios de uma **API REST**, utilizando corretamente os verbos HTTP.

---

## 🔗 Rotas Disponíveis

### Alunos

* `GET /alunos`
* `POST /alunos`
* `PUT /alunos/<id>`
* `DELETE /alunos/<id>`

### Professores

* `GET /professor`
* `POST /professor`
* `PUT /professor/<id>`
* `DELETE /professor/<id>`

---

## 📦 Formato das Respostas

As respostas da API são retornadas no formato **JSON**, utilizando o método `jsonify`, facilitando a integração com outras aplicações e frontends.

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/PabloVavrik/api_sistema_escolar.git
```

2. Acesse o diretório do projeto:

```bash
cd api_sistema_escolar
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

4. Instale as dependências:

```bash
pip install flask
```

5. Execute a aplicação:

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 🧪 Próximos Passos

* Integração com banco de dados **SQLite** para persistência dos dados
* Implementação de **Testes Unitários**
* Documentação da API
* Evolução para um cenário mais próximo de produção

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com foco em **aprendizado prático**, visando consolidar conhecimentos em:

* Desenvolvimento Backend
* APIs REST
* Organização e arquitetura de código
* Boas práticas de programação

---

## 👤 Autor

**Pablo Neves Vavrik**
Estudante de Análise e Desenvolvimento de Sistemas
Foco em Backend, APIs e Python

🔗 GitHub: [https://github.com/PabloVavrik](https://github.com/PabloVavrik)
🔗 LinkedIn: [https://www.linkedin.com/in/pablovavrik](https://www.linkedin.com/in/pablovavrik)

