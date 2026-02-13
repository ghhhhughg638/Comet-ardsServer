import asyncio
import json
from collections import deque

import jwt
import websockets

from config import host, ws_port, JWT_algorithm, JWT_KEY
from database import db, User
from timez import Timez_Create_Now


class WebSocketServer:
    def __init__(self):
        self.user = None
        self.algorithm = JWT_algorithm
        self.secret_key = JWT_KEY
        self.id_to_websocket = {}  #id的字典
        self.waiting_queue = deque()  #匹配队列中的玩家
        self.player_deck = {}  #匹配的玩家对应的卡组
        self.playing_queue = {}  #正在比赛的玩家
        self.match = {}  #正在进行的比赛
        self.match_id = 0
        self.lock = asyncio.Lock()  # 创建锁

    async def JWT_Check(self, websocket):
        """从HTTP头中提取用户ID"""
        try:

            headers = websocket.request.headers
            auth_header = headers.get('Authorization')

            if auth_header is None:
                await websocket.close(code=1008, reason="Authentication required")
                return False

            token = auth_header.replace("JWT ", "")
            payload_client = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm]
            )
            user_id: str = payload_client.get("user_id")
            user = await db.Find_user_data(list_name="id", data=user_id)
            payload_server = jwt.decode(
                user.player_JWT,
                self.secret_key,
                algorithms=[self.algorithm]
            )
            if abs(payload_client.get("exp") - payload_server.get("exp")) < 86400:
                pass
            else:
                await websocket.close(code=1008, reason="Authentication required")
                return False

            self.user: User = user
            return True
        except Exception as e:
            print(e)
            await websocket.close(code=1008, reason="Authentication required")
            return False

    async def Send_To_Id(self, conn_id: int, message) -> bool:
        """
        发送消息给指定ID的客户端
        conn_id: 客户端ID
        message: 要发送的消息
        返回: 是否发送成功
        """
        # 1. 查找websocket
        print('进入函数')
        if conn_id in self.id_to_websocket:
            pass
        else:
            print(self.id_to_websocket)
            print('不存在')
            return False  # ID不存在

        websocket = self.id_to_websocket[conn_id]
        try:
            print(message)
            await websocket.send(message)
            return True
        except Exception as e:
            print(e)
            return False

    async def add_match_players(self, conn_id: int, deck_id: int):
        """新增匹配玩家"""
        async with self.lock:
            print('进入方法体')
            if conn_id in self.waiting_queue or conn_id in self.playing_queue:
                print('不符合条件')
                return False
            self.player_deck[conn_id] = deck_id
            self.waiting_queue.append(conn_id)
            if len(self.waiting_queue) >= 2:
                # 从队列头部取出两个玩家
                player1 = self.waiting_queue.popleft()
                player2 = self.waiting_queue.popleft()

                # 创建比赛
                await self.Create_Match(player1, player2)
                return True
            else:
                print('玩家数太少')
                return False

    async def Create_Match(self, player1: int, player2: int):
        self.playing_queue[player1] = self.match_id
        self.playing_queue[player2] = self.match_id
        self.match[self.match_id] = {
            'player_left': player1,
            'player_right': player2,
            'player_status_left': 'not_done',
            "player_status_right": "not_done",  #等待右侧开局换牌完成
            "match_type": "battle",  #比赛类型对战
            "current_turn": 1,  #当前回合数
            "actions": [],  # 动作历史记录
            "current_action_id": 0,  # 当前动作ID
            "left_is_online": 1,  #左侧玩家是否在线
            "deck_id_left": self.player_deck[player1],  # 左侧玩家卡组ID
            "right_is_online": 1,  #右侧玩家是否在线
            "deck_id_right": self.player_deck[player2],  # 右侧玩家卡组ID
            "start_side": "left",  #先手玩家
            "status": "pending",  #比赛状态，pending等待中
            "notifications": [],  # 通知列表
            "winner_id": 0,  #胜利者,0表示无
            "winner_side": ""  #胜利方,空字符串表示无
        }
        self.match_id += 1
        return True

    async def handle_client(self, websocket):

        if await self.JWT_Check(websocket=websocket):
            # 分配ID
            conn_id = self.user.id
            websocket.conn_id = conn_id  # 挂在连接对象上
        else:
            return

        self.id_to_websocket[conn_id] = websocket
        print(self.id_to_websocket)
        try:
            async for message in websocket:
                try:
                    # 解析JSON消息
                    data = json.loads(message)

                    # 检查是否是ping消息
                    if (data.get("channel") == "ping" and
                            data.get("message") == "ping"):
                        # 构建响应
                        response = {
                            "message": "pong",
                            "channel": "ping",
                            "context": "",
                            "timestamp": await Timez_Create_Now(),
                            "sender": websocket.conn_id,
                            "receiver": ""
                        }

                        # 发送响应
                        await websocket.send(json.dumps(response))
                        continue  # 跳过后续处理
                except json.JSONDecodeError:
                    # 如果不是JSON，按原样处理
                    await websocket.send(f"Echo: {message}")
        finally:
            del self.id_to_websocket[conn_id]

    async def start(self, host=host, port=ws_port):
        async with websockets.serve(self.handle_client, host, port):
            await asyncio.Future()


server = WebSocketServer()
