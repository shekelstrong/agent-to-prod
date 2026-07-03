"""scale_horizontally: горизонтальное масштабирование."""


async def run(current_users: int, target_users: int, service_type: str) -> dict:
    """Стратегия масштабирования.

    Args:
        current_users: Текущих.
        target_users: Целевых.
        service_type: api/bot/web/worker.

    Returns:
        Словарь со стратегией.
    """
    growth = target_users / max(current_users, 1)

    return {
        "current_users": current_users,
        "target_users": target_users,
        "growth_factor": round(growth, 1),
        "service_type": service_type,
        "principles": [
            "Stateless — никакого local state (только DB/Redis)",
            "Horizontal scaling — добавляем instances, а не RAM/CPU",
            "Load balancer перед всеми instances",
            "Database connection pooling (PgBouncer / SQLAlchemy pool)",
            "Cache (Redis) перед DB для hot paths",
            "Async workers для долгих задач (LLM, video, email)",
        ],
        "by_scale": [
            {"users": "1k", "instances": "1", "db": "single Postgres", "cache": "none", "queue": "none"},
            {"users": "10k", "instances": "2-3 + LB", "db": "Postgres + replicas", "cache": "Redis", "queue": "Celery/RQ"},
            {"users": "100k", "instances": "5-10 + LB + autoscaling", "db": "Postgres + read replicas + connection pooler", "cache": "Redis cluster", "queue": "Celery workers"},
            {"users": "1M+", "instances": "20-100 + K8s/HPA", "db": "Sharded / Vitess / managed", "cache": "Redis + CDN", "queue": "Kafka"},
        ],
        "checklist": [
            "Healthcheck на каждом instance",
            "Graceful shutdown (drain connections перед SIGTERM)",
            "Idempotency keys для повторяющихся запросов",
            "Rate limiting per user/IP",
            "Sticky sessions НЕ нужны если stateless",
            "Sticky sessions НЕ нужны если нет WebSocket",
        ],
        "by_service_type": {
            "api": "FastAPI/Uvicorn workers, gunicorn multi-worker",
            "bot": "Long polling, single instance (Telegram не любит multiple)",
            "web": "CDN + edge cache, ISR для Next.js",
            "worker": "Celery/RQ с autoscaling по queue length",
        },
    }
