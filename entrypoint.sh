#!/bin/sh

# Запустить сервер FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000

exec "$@"