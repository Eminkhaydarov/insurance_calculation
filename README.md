# insurance_calculation
REST API сервис по расчёту стоимости страхования в зависимости от типа груза и объявленной стоимости (ОС).
## Stack
- FastAPI
- PostgreSQL
- Tortoise ORM
- Docker
- Docker-compose

## Запуск
- Указать свои данные для подключемния к базе данных или уоставить их тестовыми
- Запустить контейнер командой:
```
docker-compose -f docker-compose.yml up -d
```
