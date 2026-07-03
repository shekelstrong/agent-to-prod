---
name: agent-to-prod
description: AI-агент / продукт от ТЗ до production. Системный дизайн, MVP за 4 недели, чек-лист прод-деплоя (security/performance/reliability), Golden Signals мониторинг, горизонтальное масштабирование, blameless post-mortem.
---

# Agent to Prod

MCP-сервер для вывода AI-продукта в production.

## Когда использовать

- Запускаешь новый AI-агент / продукт
- Не знаешь с чего начать — нужна архитектура
- Готовишься к прод-деплою — нужен чек-лист
- Масштабируешь существующий сервис
- Был инцидент — нужен blameless post-mortem
- Делаешь MVP и хочешь timeline + метрики

## 6 tools pipeline

```
идея → build_mvp (4 недели) → deploy_production (чек-лист) → setup_monitoring (алерты)
       ↓
   design_architecture (системный дизайн)
       ↓
   scale_horizontally (когда вырастет)
       ↓
   post_mortem (когда что-то сломалось)
```

## Алгоритм

### 1. design_architecture
7 компонентов:
- Frontend (Next.js, Vite)
- API Gateway (FastAPI)
- Backend Services
- Database (PostgreSQL + Redis)
- Queue (Celery, n8n)
- Storage (S3, MinIO)
- Observability (Prometheus, Grafana, Sentry)

3 масштаба: small (1k) / medium (10k) / large (100k+).

### 2. build_mvp
4 недели:
- W1: скелет (auth, БД, hello world)
- W2: главная фича end-to-end
- W3: деплой + Sentry + аналитика + лендинг
- W4: первые 10 юзеров + feedback

**MVP = минимально жизнеспособный, не минимально приятный.**

### 3. deploy_production
40+ пунктов в 5 категориях:
- **Security**: HTTPS, auth, SQLi/XSS, rate limit, secrets, CORS
- **Performance**: CDN, p95 < 200ms, bundle < 300KB, cache
- **Reliability**: backups, healthcheck, restart policy, multi-instance
- **Monitoring**: latency p95, error rate, throughput, alerts
- **Operations**: CI/CD, rollback, runbook, on-call

### 4. setup_monitoring
4 Golden Signals:
- **Latency**: p50/p95/p99 по endpoint
- **Traffic**: req/sec
- **Errors**: 5xx rate
- **Saturation**: CPU/RAM/disk

+ business metrics (DAU, conversion, churn) + alerts в Telegram.

### 5. scale_horizontally
Принципы: stateless, horizontal scaling, LB, DB connection pool, cache, async workers.
4 масштаба: 1k / 10k / 100k / 1M+ users.

### 6. post_mortem
Blameless формат (Google SRE book):
- Summary / Impact / Timeline
- Root cause (не "что делали", а "почему сломалось")
- Why we didn't catch earlier
- What went well / poorly
- Action items с owner + due date
- Lessons learned

## Pitfalls

| Ошибка | Последствие | Как избежать |
|---|---|---|
| MVP на 3 месяца | Не MVP, монстр | Жёсткий scope: 1-2 фичи |
| Sync вызовы к LLM | API timeout | Async workers + queue |
| Файлы на диске сервера | Потеря при redeploy | S3 / MinIO |
| Без мониторинга | Узнаёшь о падении от юзеров | Sentry + Prometheus с первого дня |
| Stateful API | Нельзя масштабировать | Stateless + DB/Redis |
| Нет runbook | On-call дебаг по 3 ночи | Runbook на типичные ошибки |
| Auto-rollback не настроен | Hotfix = 1 час паники | Health-check → auto-rollback |
| Blame в post-mortem | Люди скрывают ошибки | Blameless → фокус на системе |

## Источники

6 скиллов: autonomous-ai-agents, buildo-deployment-architecture, python-vps-deployment, telegram-bot-docker-deploy, subagent-driven-development, systematic-debugging.
