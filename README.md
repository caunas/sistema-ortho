# Sistema Ortho

Sistema web fullstack para gerenciamento clínico odontológico/ortodôntico, desenvolvido com foco em autenticação, gestão de pacientes e estrutura SaaS-ready.

> Projeto desenvolvido como MVP funcional com deploy em produção utilizando Docker, NGINX, PostgreSQL e CI/CD.

---

# ✨ Funcionalidades

- [x] Autenticação de usuários
- [x] Dashboard autenticado
- [x] Listagem de pacientes
- [x] Estrutura modular baseada em apps Django
- [x] Configuração preparada para ambiente de produção

---

# ⚙ Stack Utilizada

## Backend
- Python 3.12
- Django 6
- PostgreSQL
- Gunicorn

## Frontend
- Django Templates
- HTML/CSS/JS

---

# 🚀 Deploy Rápido

## 1. Preparando o ambiente
Apenas certifique-se de ter o Docker instalado na versão mais recente

## 2. Clonagem e instalação
```bash
git clone https://github.com/parallax-ds/sistema-ortho.git
cd sistema-ortho
```

## 3. Configuração do projeto

- Variáveis de ambiente
Crie um arquivo ```.env``` com as variáveis de ambiente, usando ```.env.example``` como base.

```toml
# APP

# DEVELOPMENT or PRODUCTION
APP_ENV=
APP_DEBUG=
SECRET_KEY=
# LISTE OS ALLOWED HOSTS QUE O DJANGO IRÁ PERMITIR, SEPARE-OS COM VÍRGULA.
ALLOWED_HOSTS=localhost, 127.0.0.1

# DATABASE (Docker)
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

# POSTGRES (container)
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```
Os valores de DB, USER e PASSWORD devem ser os mesmos tanto para POSTGRES quanto para DATABASE.

## 4. Executar projeto
```bash
docker compose up --build
```
> As migrações já são feitas automaticamente assim que o banco de dados estiver saudável.

Para que seja possível acessar a aplicação, crie um superusuário.
```bash
docker compose exec web python manage.py createsuperuser
```

Com o projeto rodando, acesse ```127.0.0.1:8000``` do seu navegador, você deve ver a página de login do Sistema Ortho!

---

# 🌐 Deploy

O projeto foi estruturado para deploy em VPS Linux utilizando:

- Docker Compose
- NGINX Reverse Proxy
- HTTPS com Certbot
- PostgreSQL persistente

---

# 📌 Status do Projeto

Atualmente o projeto encontra-se como MVP funcional e serve como:

- estudo de arquitetura fullstack,
- laboratório de deploy e infraestrutura,
- projeto de portfólio.
