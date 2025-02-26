# DESAFIO LOGIN
Este projeto faz parte de um desafio técnico, utilizando Django Framework, que consiste em criar uma tela login e cadastro para um site, com as devidas validações.

## Técnologias utilizadas
- Python 3.11.2
- Django 5.1.6
- Dotenv
- PostgreSQL
- HTML, CSS, Javascript, AJAX, Bootstrap

## Instalação
### 1. **Clone o repositório**

```sh
git clone https://github.com/albertojbe/desafiologin.git
cd desafio-login
```

### 2. **Crie e ative o ambiente virtual**

`Linux`
```sh
python3 -m venv venv
source venv/bin/activate
```
`Windows`
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. **Instale as dependências**
```sh
pip install -r requirements.txt
```

### 4. **Configure o banco de dados e variáveis de ambiente**

Crie um arquivo ``.env`` na pasta raiz do projeto e sete as seguintes variávies:
```sh
# Configuração do Django
SECRET_KEY=sua_chave_secreta

# Configuração do banco de dados PostgreSQL
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

# Configuração de e-mail (para envio de emails pelo Django)
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha
```

### 5. **Realize as migrações no banco de dados**
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. **Execute a aplicação**
```sh
python manage.py runserver
```
Acesse [127.0.0.1:8000](127.0.0.1:8000) no seu navegador
