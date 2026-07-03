"""build_mvp: план MVP."""


async def run(idea: str, weeks: int = 4) -> dict:
    """План MVP.

    Args:
        idea: Идея.
        weeks: Сколько недель.

    Returns:
        План MVP.
    """
    return {
        "idea": idea,
        "timeline_weeks": weeks,
        "scope": {
            "in_scope": [
                "1-2 ключевые фичи (то без чего продукт не имеет смысла)",
                "Auth (email + password минимум)",
                "1 main user flow (от входа до результата)",
                "Базовый UI (не идеальный, но рабочий)",
                "Логирование и базовая аналитика",
            ],
            "out_of_scope": [
                "Все edge cases (добавим после PMF)",
                "Mobile app (если web работает)",
                "Интеграции с 10 сервисами (начни с 1-2)",
                "Платные фичи (докажи ценность бесплатно)",
                "Marketing site (лендинг можно за 1 день)",
            ],
        },
        "week_by_week": [
            {"week": 1, "goal": "Скелет", "deliverables": ["Auth (email)", "БД + миграции", "Базовый UI", "Hello world endpoint"]},
            {"week": 2, "goal": "Главная фича", "deliverables": ["Core feature end-to-end", "Wireframe → working code", "Manual test с 5 друзьями"]},
            {"week": 3, "goal": "Полировка + деплой", "deliverables": ["Deploy на Vercel/VPS", "Error tracking (Sentry)", "Basic analytics", "Landing page"]},
            {"week": 4, "goal": "Первые 10 пользователей", "deliverables": ["Outreach в TenChat/VC/соцсети", "Feedback loop", "Roadmap v2"]},
        ],
        "metrics": [
            "Time-to-first-value (от регистрации до результата) < 5 минут",
            "Retention day-1 > 30% (зритель вернулся на следующий день)",
            "NPS > 30 (готов рекомендовать)",
        ],
        "anti_patterns": [
            "MVP на 3 месяца — это уже не MVP",
            "Каждая фича 'необходима' — нет, убери половину",
            "Идеальный дизайн с первого дня — нет, ugly + working",
            "Ждать пока 'всё будет готово' — зарелизь на неделе 3",
        ],
    }
