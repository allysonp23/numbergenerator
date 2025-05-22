# Number Generator API

API para gerar números fictícios:
- CPF
- CNPJ
- Contas bancárias
- Telefones
- Nomes
- Textos Lorem Ipsum

Este projeto utiliza:
- Django + Django REST Framework
- Celery com Redis como broker de filas
- PostgreSQL como banco de dados
- OAuth2 (django-oauth-toolkit) para autenticação
- Swagger (drf-yasg) para documentação
- Docker e docker-compose para orquestração de containers
- Make para comandos de automação

## Pré-requisitos
- Docker
- Docker Compose
- Make (opcional)

## Iniciando com Make
No diretório raiz do projeto:

```bash
# Build e sobe tudo em background
make up

# Ver logs em tempo real
make logs

# Para e remove containers/volumes
make down
```

## Executando sem Make
```bash
docker-compose up --build
```

## Endpoints principais
- Swagger UI: http://localhost:8000/swagger/
- Gera CPF:   GET /api/cpf/?mask=true
- Gera CNPJ:  GET /api/cnpj/?mask=true
- Gera Conta: GET /api/bankaccount/
- Outros: /api/lorem/, /api/phone/, /api/names/

## Autenticação (OAuth2)
1. Crie super-usuário:
   ```bash
    docker-compose exec web python manage.py createsuperuser
```
2. No Django Admin (/admin/), registre uma Application em OAuth2 Provider.
3. Obtenha token:
   ```bash
curl -X POST http://localhost:8000/o/token/ \
  -d 'grant_type=password' \
  -d 'username=<user>' \
  -d 'password=<pass>' \
  -d 'client_id=<ID>' \
  -d 'client_secret=<SECRET>'
```
4. Use o token nas requisições:
   ```bash
    curl http://localhost:8000/api/cnpj/?mask=true \
    -H 'Authorization: Bearer <access_token>'
```

## Comandos úteis
- `make migrate` : aplica migrations
- `make shell`   : abre Django shell
- `make celery`  : inicia worker Celery
- `make superuser` : cria um superusuário Django

## Contribuindo
Pull requests são bem-vindos. Abra issues para bugs ou melhorias.

## Licença
MIT