# Bot Birthday

Aplicação Django para cadastro de aniversários e envio de mensagens em grupo do WhatsApp via Evolution API.

## Funcionalidades

- CRUD simples de aniversários (nome, data de nascimento)
- Templates com base + lista + formulário
- Envio de mensagem com aniversariantes do dia (Evolution API)
- Ambiente Docker com PostgreSQL

## Requisitos

- Docker e Docker Compose
- Conta/instância do Evolution API (container incluso)
- Opcional: Python 3.12 para rodar localmente sem Docker

## Estrutura

```
bot_birthday/
├─ birthday/                # App Django
│  ├─ models.py             # Birthdays model
│  ├─ forms.py              # BirthdaysForm
│  ├─ views.py              # create/list + endpoint opcional
│  ├─ urls.py               # rotas do app
│  └─ services.py           # integração Evolution API
├─ core/                    # Projeto Django
│  ├─ settings.py           # configurações e env vars
│  └─ urls.py               # inclui rotas do app
├─ templates/
│  ├─ base.html
│  └─ birthday/
│     ├─ list.html
│     └─ forms.html
├─ static/
│  └─ style.css
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ .env                     # vars para Evolution API (exemplo abaixo)
└─ manage.py
```

## Configuração

Settings principais (via variáveis de ambiente):
- Banco: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- Debug/hosts: `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS`
- Evolution API: `EVOLUTION_API_BASE_URL`, `EVOLUTION_API_INSTANCE`, `EVOLUTION_API_TOKEN`, `EVOLUTION_API_GROUP_JID`

Exemplo de `.env` para Evolution API:
```
DATABASE_ENABLED=true
DATABASE_PROVIDER=postgres
DATABASE_URL=postgres://birthday:birthdaypass@db:5432/bot_birthday
```

## Docker

Compose com três serviços: `db` (Postgres), `web` (Django) e `evolution-api`.

Como iniciar:
```
docker compose up --build
```

Acessos:
- Django: http://localhost:8000/aniversarios/
- Evolution API: http://localhost:8080

Comandos úteis:
- Migrar banco: `docker compose run --rm web python manage.py migrate`
- Criar superusuário: `docker compose run --rm web python manage.py createsuperuser`
- Enviar mensagem (management command): `docker compose run --rm web python manage.py send_birthday_messages`
