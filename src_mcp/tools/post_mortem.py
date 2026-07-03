"""post_mortem: шаблон пост-мортема."""


async def run(incident: str) -> dict:
    """Генерирует шаблон пост-мортема.

    Args:
        incident: Описание инцидента.

    Returns:
        Словарь с секциями.
    """
    return {
        "incident": incident,
        "template": {
            "summary": "Что произошло, в одном абзаце",
            "impact": "Сколько пользователей/запросов затронуто, длительность, revenue loss",
            "timeline": [
                {"time": "T+0", "event": "Деплой с багом в production"},
                {"time": "T+15min", "event": "Алерт в Telegram от Sentry"},
                {"time": "T+20min", "event": "On-call инженер подключился"},
                {"time": "T+45min", "event": "Hotfix задеплоен"},
                {"time": "T+60min", "event": "100% трафика восстановлено"},
            ],
            "root_cause": "Что именно сломалось. Не 'что мы делали' а 'почему это вызвало падение'",
            "why_we_didnt_catch_earlier": [
                "Тест был, но не покрывал этот edge case",
                "Алерт был, но threshold был слишком высокий",
                "Код-ревью было, но reviewer не знал эту область",
            ],
            "what_went_well": [
                "Алерт сработал в течение 15 минут",
                "Hotfix был готов за 25 минут",
                "Коммуникация с пользователями была прозрачной",
            ],
            "what_went_poorly": [
                "Нет автоматического rollback",
                "Тест не покрывал этот путь",
                "Документации по runbook не было",
            ],
            "action_items": [
                {"action": "Добавить test на edge case", "owner": "X", "due": "YYYY-MM-DD"},
                {"action": "Починить threshold алерта", "owner": "Y", "due": "YYYY-MM-DD"},
                {"action": "Настроить auto-rollback при > 5% error rate", "owner": "Z", "due": "YYYY-MM-DD"},
            ],
            "lessons_learned": [
                "Edge case покрыт — production ready",
                "Threshold алертов нужно снизить",
                "Auto-rollback экономит часы on-call",
            ],
        },
        "principles": [
            "Blameless — фокус на системе, а не на человеке",
            "Action items конкретные, с owner и датой",
            "Lessons learned = что МЕНЯЕМ в процессе",
            "Публичный пост-мортем (Google SRE book) = trust",
        ],
    }
