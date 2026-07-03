# agent-to-prod

> MCP-сервер: AI-агент от ТЗ до production. Архитектура, MVP, прод-деплой, мониторинг, масштабирование, пост-мортем.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![MCP](https://img.shields.io/badge/MCP-compatible-purple.svg)](https://modelcontextprotocol.io)

## 🎯 Что это

MCP-сервер с 6 инструментами для вывода продукта в production:

- 🏗 **design_architecture** — системный дизайн (компоненты, потоки данных, выбор стека)
- 🚀 **build_mvp** — план MVP (4 недели, scope, timeline, метрики успеха)
- 🔒 **deploy_production** — чек-лист прод-деплоя (security/performance/reliability/monitoring)
- 📊 **setup_monitoring** — Golden Signals, алерты, dashboards
- 📈 **scale_horizontally** — стратегия масштабирования (stateless, LB, queue, cache)
- 📋 **post_mortem** — blameless шаблон (timeline, root cause, action items)

## 📦 Установка

```bash
git clone https://github.com/shekelstrong/agent-to-prod.git
cd agent-to-prod
pip install -r requirements.txt
```

## 🛠 MCP Tools

### design_architecture
```python
result = await design_architecture.run("CRM для SMB", scale="small")
# → {components, data_flows, decisions, anti_patterns}
```

3 масштаба: small (1k users), medium (10k), large (100k+).

### build_mvp
```python
result = await build_mvp.run("AI-тьютор английского", weeks=4)
# → {scope, week_by_week, metrics, anti_patterns}
```

Week 1: скелет. Week 2: главная фича. Week 3: деплой. Week 4: первые 10 юзеров.

### deploy_production
```python
result = await deploy_production.run("my-api")
# → {checklist: [Security, Performance, Reliability, Monitoring, Operations]}
```

40+ пунктов чек-листа по 5 категориям.

### setup_monitoring
```python
result = await setup_monitoring.run("my-api", "Prometheus+Grafana")
# → {golden_signals, business_metrics, alerts, dashboards, tools}
```

4 Golden Signals: Latency, Traffic, Errors, Saturation.

### scale_horizontally
```python
result = await scale_horizontally.run(1000, 100000, "api")
# → {principles, by_scale, checklist, by_service_type}
```

Масштабы: 1k / 10k / 100k / 1M+ users.

### post_mortem
```python
result = await post_mortem.run("API упал на 45 минут")
# → {template: {summary, impact, timeline, root_cause, action_items, ...}}
```

Blameless формат.

## 📁 Структура

```
agent-to-prod/
├── README.md
├── LICENSE
├── SKILL.md
├── requirements.txt
├── src_mcp/
│   ├── server.py
│   └── tools/
│       ├── design_architecture.py
│       ├── build_mvp.py
│       ├── deploy_production.py
│       ├── setup_monitoring.py
│       ├── scale_horizontally.py
│       └── post_mortem.py
└── .github/workflows/ci.yml
```

## 🎯 Golden Signals (SRE)

| Signal | PromQL | Alert |
|---|---|---|
| Latency | `histogram_quantile(0.95, ...)` | > 500ms |
| Traffic | `rate(http_requests_total[5m])` | аномалия |
| Errors | `rate(5xx) / rate(total)` | > 1% |
| Saturation | `100 - cpu_idle` | > 80% |

## 📄 License

MIT © Vasiliy Nedopekin (shekelstrong)
