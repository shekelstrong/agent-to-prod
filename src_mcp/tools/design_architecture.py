"""design_architecture: системный дизайн."""


async def run(product: str, scale: str = "small") -> dict:
    """Генерирует архитектурный план.

    Args:
        product: Что за продукт.
        scale: small / medium / large.

    Returns:
        Словарь с архитектурой.
    """
    return {
        "product": product,
        "scale": scale,
        "components": [
            {"name": "Frontend (Web/Mobile)", "stack": _frontend_stack(scale), "responsibility": "UI, роутинг, стейт"},
            {"name": "API Gateway", "stack": "FastAPI / Express / NestJS", "responsibility": "Auth, rate limit, routing"},
            {"name": "Backend Services", "stack": _backend_stack(scale), "responsibility": "Бизнес-логика, оркестрация"},
            {"name": "Database", "stack": "PostgreSQL + Redis", "responsibility": "Primary data + кэш"},
            {"name": "Queue (async)", "stack": "Celery / BullMQ / n8n", "responsibility": "Долгие задачи, уведомления"},
            {"name": "Storage (files)", "stack": "S3 / MinIO", "responsibility": "Изображения, видео, документы"},
            {"name": "Observability", "stack": "Prometheus + Grafana + Sentry", "responsibility": "Метрики, логи, ошибки"},
        ],
        "data_flows": [
            "User → Frontend → API Gateway → Backend Service → Database",
            "Backend → Queue → Worker (async обработка)",
            "User upload → API → S3 (через pre-signed URL)",
            "Service → Sentry (errors), Prometheus (metrics)",
        ],
        "decisions": [
            "Stateless API — легко масштабировать горизонтально",
            "Database connection pooling (PgBouncer / SQLAlchemy pool)",
            "Cache (Redis) перед DB для hot keys",
            "Async workers для email, video processing, AI-вызовов",
            "Secrets через env, не в коде (Vault / Doppler / .env + .gitignore)",
        ],
        "anti_patterns": [
            "Monolith без границ (сложно масштабировать)",
            "Sync вызовы к медленным API (LLM, video) — блокируют request",
            "Хранить файлы на диске сервера (потеряются при deploy)",
            "Без мониторинга (узнаешь о падении от пользователей)",
        ],
    }


def _frontend_stack(scale: str) -> str:
    if scale == "small":
        return "Next.js 14 + Tailwind"
    elif scale == "medium":
        return "Next.js + Vite (admin) + React Native (mobile)"
    return "Next.js + Micro-frontends"


def _backend_stack(scale: str) -> str:
    if scale == "small":
        return "Python/FastAPI (1-2 сервиса)"
    elif scale == "medium":
        return "Python/FastAPI + 3-5 сервисов"
    return "Polyglot: Python/Go/Node по доменам"
