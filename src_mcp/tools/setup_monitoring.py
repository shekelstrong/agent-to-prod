"""setup_monitoring: настройка мониторинга."""


async def run(service: str, stack: str = "Prometheus+Grafana") -> dict:
    """План мониторинга.

    Args:
        service: Сервис.
        stack: Стек (Prometheus+Grafana, Datadog, Sentry-only, ...).

    Returns:
        Словарь с метриками и алертами.
    """
    return {
        "service": service,
        "stack": stack,
        "golden_signals": [
            {"name": "Latency", "promql": 'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))', "alert": "> 500ms"},
            {"name": "Traffic", "promql": 'rate(http_requests_total[5m])', "alert": "аномалия"},
            {"name": "Errors", "promql": 'rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])', "alert": "> 1%"},
            {"name": "Saturation", "promql": '100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)', "alert": "> 80%"},
        ],
        "business_metrics": [
            "Daily Active Users (DAU)",
            "New signups per day",
            "Conversion rate (signups → activated users)",
            "Revenue per day / MRR",
            "Churn rate (отток за неделю)",
        ],
        "alerts": [
            {"name": "API down", "condition": "error_rate > 50% for 2m", "channel": "Telegram + SMS"},
            {"name": "Slow response", "condition": "p95 latency > 2s for 5m", "channel": "Telegram"},
            {"name": "Database issue", "condition": "connection pool exhausted", "channel": "Telegram + email"},
            {"name": "Disk full", "condition": "disk usage > 90%", "channel": "Telegram"},
        ],
        "dashboards": [
            "Overview: requests/sec, p95 latency, error rate, active users",
            "Per-endpoint: latency histogram, top slow endpoints, error breakdown",
            "Database: connections, slow queries, replication lag",
            "Infrastructure: CPU, RAM, disk, network",
        ],
        "tools": {
            "metrics": "Prometheus + Grafana (бесплатно, self-hosted)",
            "logs": "Loki / Vector / ELK",
            "errors": "Sentry (бесплатный план)",
            "uptime": "UptimeRobot / BetterStack (бесплатно)",
            "alerts": "Alertmanager → Telegram / Slack",
        },
    }
