import asyncio

import uvicorn

from app import app
from config import *
from database import db
from websocket import server


async def initialize_database():
    """初始化数据库"""
    print("🔄 正在初始化数据库连接...")
    await db.initialize()
    await db.create_tables()
    print("✅ 数据库初始化完成")


async def start_websocket_server():
    """启动WebSocket服务器"""

    await server.start()


async def start_http_server():
    """启动HTTP服务器"""
    config = uvicorn.Config(
        app,
        host=host,
        port=port,
        server_header=False,
        date_header=False,
    )
    print('kkk')
    http_server = uvicorn.Server(config)
    await http_server.serve()


async def main():
    """同时启动HTTP和WebSocket服务器"""
    await initialize_database()
    http_task = asyncio.create_task(start_http_server())  # 启动HTTP服务器
    websocket_task, periodic_task = await start_websocket_server()  # 启动WebSocket服务器
    await asyncio.gather(http_task, websocket_task, periodic_task)  # 等待所有任务完成


def run_servers():
    """运行所有服务器"""
    asyncio.run(main())


if __name__ == '__main__':
    run_servers()
