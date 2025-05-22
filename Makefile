.PHONY: up down restart build migrate shell logs celery superuser jwt apikey

up:
	@echo "Building and starting all services..."
	docker-compose up --build -d

down:
	@echo "Stopping and removing containers..."
	docker-compose down -v

restart: down up

build:
	@echo "Building images..."
	docker-compose build

mkm:
	@echo "Creating migrations..."
	docker-compose exec web python manage.py makemigrations
	
migrate:
	@echo "Applying Django migrations..."
	docker-compose exec web python manage.py migrate

shell:
	@echo "Opening Django shell..."
	docker-compose exec web python manage.py shell

celery:
	@echo "Starting Celery worker..."
	docker-compose up -d celery

logs:
	@echo "Attaching to logs..."
	docker-compose logs -f

superuser:
	@echo "Creating Django superuser..."
	docker-compose exec web python manage.py createsuperuser

apikey:
	@echo "Generating API key for $(name)..."
	docker-compose exec web python manage.py shell -c "from rest_framework_api_key.models import APIKey; key, _ = APIKey.objects.create_key(name='$(name)'); print('API Key:', key)"
