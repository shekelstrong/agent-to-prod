"""Agent-to-Prod MCP Server."""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from src_mcp.tools import design_architecture, build_mvp, deploy_production, setup_monitoring, scale_horizontally, post_mortem


app = Server("agent-to-prod")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="design_architecture",
            description="Системный дизайн: компоненты, потоки данных, выбор стека.",
            inputSchema={
                "type": "object",
                "properties": {
                    "product": {"type": "string", "description": "Что за продукт"},
                    "scale": {"type": "string", "enum": ["small", "medium", "large"], "default": "small"},
                },
                "required": ["product"],
            },
        ),
        Tool(
            name="build_mvp",
            description="План MVP: scope, features, tech stack, timeline, метрики успеха.",
            inputSchema={
                "type": "object",
                "properties": {
                    "idea": {"type": "string"},
                    "weeks": {"type": "integer", "default": 4},
                },
                "required": ["idea"],
            },
        ),
        Tool(
            name="deploy_production",
            description="Чек-лист прод-деплоя: security, performance, monitoring, backups, rollback.",
            inputSchema={
                "type": "object",
                "properties": {
                    "service": {"type": "string", "description": "Что за сервис"},
                },
                "required": ["service"],
            },
        ),
        Tool(
            name="setup_monitoring",
            description="Настройка мониторинга: метрики (latency, errors, throughput), алерты, dashboards.",
            inputSchema={
                "type": "object",
                "properties": {
                    "service": {"type": "string"},
                    "stack": {"type": "string", "default": "Prometheus+Grafana"},
                },
                "required": ["service"],
            },
        ),
        Tool(
            name="scale_horizontally",
            description="Стратегия горизонтального масштабирования: load balancer, stateless, queue, кэш.",
            inputSchema={
                "type": "object",
                "properties": {
                    "current_users": {"type": "integer"},
                    "target_users": {"type": "integer"},
                    "service_type": {"type": "string", "enum": ["api", "bot", "web", "worker"]},
                },
                "required": ["current_users", "target_users", "service_type"],
            },
        ),
        Tool(
            name="post_mortem",
            description="Шаблон post-mortem: timeline, root cause, impact, lessons, action items.",
            inputSchema={
                "type": "object",
                "properties": {
                    "incident": {"type": "string", "description": "Описание инцидента"},
                },
                "required": ["incident"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    import json
    tools_map = {
        "design_architecture": design_architecture,
        "build_mvp": build_mvp,
        "deploy_production": deploy_production,
        "setup_monitoring": setup_monitoring,
        "scale_horizontally": scale_horizontally,
        "post_mortem": post_mortem,
    }
    try:
        result = await tools_map[name].run(**arguments)
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {type(e).__name__}: {e}")]


async def main():
    async with stdio_server() as (rs, ws):
        await app.run(rs, ws, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
