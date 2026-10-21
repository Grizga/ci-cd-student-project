# CI/CD Student Project

![CI Status](https://github.com/Grizga/ci-cd-student-project/actions/workflows/ci.yml/badge.svg)

Простой проект для демонстрации CI/CD pipeline с автоматическим тестированием.

## Структура
- `src/calculator.py` — калькулятор
- `tests/test_calculator.py` — тесты pytest
- `.github/workflows/ci.yml` — CI pipeline

## Запуск локально
```bash
pip install -r requirements.txt
pytest tests/ -v
