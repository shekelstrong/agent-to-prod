"""deploy_production: чек-лист прод-деплоя."""


async def run(service: str) -> dict:
    """Чек-лист для прод-деплоя.

    Args:
        service: Название сервиса.

    Returns:
        Чек-лист по категориям.
    """
    return {
        "service": service,
        "checklist": [
            {
                "category": "Security",
                "items": [
                    "HTTPS/TLS включён (Let's Encrypt или CloudFlare)",
                    "Auth на всех protected routes (не только UI)",
                    "SQL injection защита (parameterized queries)",
                    "XSS защита (escape HTML / CSP headers)",
                    "Rate limiting на API (например, 100 req/min/user)",
                    "Secrets через env, не в коде",
                    "CORS настроен правильно (не *)",
                    "Admin endpoints защищены (IP whitelist или 2FA)",
                ],
            },
            {
                "category": "Performance",
                "items": [
                    "Static assets через CDN",
                    "Database queries < 100ms p95",
                    "API response < 200ms p95",
                    "Bundle size frontend < 300KB gzipped",
                    "Images оптимизированы (WebP, lazy load)",
                    "Cache headers (ETag, Cache-Control)",
                ],
            },
            {
                "category": "Reliability",
                "items": [
                    "Backups daily (БД + storage)",
                    "Restore протестирован (не просто 'у нас есть бэкапы')",
                    "Healthcheck endpoint (/health → 200)",
                    "Restart policy (unless-stopped для Docker)",
                    "Multiple instances (>= 2 для stateless)",
                    "Load balancer (если нужно)",
                ],
            },
            {
                "category": "Monitoring",
                "items": [
                    "Latency p50/p95/p99 по endpoint",
                    "Error rate по endpoint",
                    "Throughput (req/sec)",
                    "Business metrics (signups, conversions)",
                    "Алерты в Telegram/Slack при аномалиях",
                    "Логи в централизованное хранилище (Loki / ELK)",
                ],
            },
            {
                "category": "Operations",
                "items": [
                    "CI/CD (auto-deploy на push в main)",
                    "Rollback plan (как откатить за 5 минут)",
                    "Runbook (что делать при типичных ошибках)",
                    "On-call rotation (кто отвечает 24/7)",
                    "Status page (если B2B)",
                ],
            },
        ],
    }
