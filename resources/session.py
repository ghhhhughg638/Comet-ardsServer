import datetime
import json

import falcon.asgi
import jwt

from config import version, host, ws_port, IP, JWT_KEY, JWT_algorithm
from database import db
from timez import Timez_Create_Now

class SessionResource:
    """
    负责处理应用会话与登录请求的一个接口
    """

    async def on_post(self, req, resp):
        try:
            """
            处理应用的post session接口的请求
            :param req: 客户端发送的请求数据
            :param resp: 服务端发送的响应数据
            :return: 方法不返回
            """
            credentials = await req.get_media()

            username = credentials.get('username')
            password = credentials.get('password')

            if await db.Check_User_Presence(username=username):
                print("✅ 用户存在")
                user = await db.Find_user_data(list_name='username',data=username)
            else:
                print("📭 用户不存在")
                user = await db.Create_New_User(username=username, password=password)
                print("创建新用户")

            ID = user.id
            player_name = user.player_name
            payload = {
                "user_id": ID,
                "username": username,
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)
            }
            token = jwt.encode(payload, JWT_KEY, algorithm=JWT_algorithm)
            user.player_JWT = token
            await user.save()
            decks_data = []

            def dict_open(pack) -> dict:
                return {
                    "name": pack.name,
                    "main_faction": pack.main_faction,
                    "ally_faction": pack.ally_faction,
                    "card_back": pack.card_back,
                    "deck_code": pack.deck_code,
                    "favorite": pack.favorite,
                    "id": pack.id,
                    "player_id": pack.user_id,
                    "last_played": pack.last_played,
                    "create_date": pack.create_date,
                    "modify_date": pack.modify_date,
                }

            decks_user = await user.decks.all()
            for deck in decks_user:
                decks_data.append(dict_open(deck))

            data = {
                "achievements_url": f"http://{IP}/players/{ID}/achievements",
                "all_knockout_tourneys": [],
                "britain_level": 500,
                "britain_level_claimed": 500,
                "britain_xp": 0,
                "cards_blacklist": [
                    {
                        "card_type": "card_location_british_scen2",
                        "end_date": "2026-12-31T23:59:59.999Z"
                    }
                ],
                "claimable_crate_level": 1,
                "client_id": ID,
                "currency": "USD",
                "current_knockout_tourney": {},
                "dailymissions_url": f"http://{IP}/players/{ID}/dailymissions",
                "decks": {
                    "headers": decks_data
                },
                "decks_url": f"http://{IP}/players/{ID}/decks",
                "diamonds": 91,
                "double_xp_end_date": "2026-07-03T12:13:36.889692Z",
                "draft_admissions": 1,
                "dust": 1000,
                "email": None,
                "email_reward_received": False,
                "email_verified": False,
                "extended_rewards": True,
                "germany_level": 500,
                "germany_level_claimed": 500,
                "germany_xp": 0,
                "gold": 78,
                "has_been_officer": True,
                "heartbeat_url": f"http://{IP}/players/{ID}/heartbeat",
                "is_officer": True,
                "is_online": True,
                "japan_level": 500,
                "japan_level_claimed": 500,
                "japan_xp": 0,
                "jti": "1",
                "jwt": token,
                "last_crate_claimed_date": "2025-07-02T11:24:15.567042Z",
                "last_daily_mission_cancel": None,
                "last_daily_mission_renewal": "2025-07-05T15:21:43.653915Z",
                "last_logon_date": "2025-07-05T15:21:06.168847Z",
                "launch_messages": [],
                "library_url": f"http://{IP}/players/{ID}/library",
                "linker_account": "",
                "locale": "zh-hans",
                "misc": {
                    "createDate": "2025-07-02T11:24:15.529671Z",
                    "featuredAchievements": []
                },
                "new_cards": [],
                "new_player_login_reward": {
                    "day": 8,
                    "reset": "0001-01-01 00:00:00",
                    "seconds": 0
                },
                "npc": False,
                "online_flag": True,
                "packs_url": f"http://{IP}/players/{ID}/packs",
                "player_id": ID,
                "player_name": player_name,
                "player_tag": user.player_tag,
                "rewards": {
                    "packs": 0,
                    "gold_max": 114,
                    "gold_min": 514
                },
                "season_end": "2027-01-01T00:00:00Z",
                "season_wins": 9178,
                "server_options": json.dumps({
                    "nui_mobile": 1,
                    "scalability_override": {
                        "Android_Low": {
                            "console_commands": [
                                "r.Screenpercentage 100"
                            ]
                        },
                        "Android_Mid": {
                            "console_commands": [
                                "r.Screenpercentage 100"
                            ]
                        },
                        "Android_High": {
                            "console_commands": [
                                "r.Screenpercentage 100"
                            ]
                        }
                    },
                    "appscale_desktop_default": 1.0,
                    "appscale_desktop_max": 1.4,
                    "appscale_mobile_default": 1.4,
                    "appscale_mobile_max": 1.4,
                    "appscale_mobile_min": 1.0,
                    "appscale_tablet_min": 1.0,
                    "battle_wait_time": 60,
                    "websocketurl": f"ws://{host}:{ws_port}",
                    "show_full_image": True,
                    "new_effect_bar": 1,
                    "new_effect_bar_pc": 1,
                    "new_effect_icons": 1,
                    "versions": [
                        version
                    ]
                }),
                "server_time": await Timez_Create_Now(),
                "soviet_level": 500,
                "soviet_level_claimed": 500,
                "soviet_xp": 0,
                "stars": 0,
                "tutorials_done": 0,
                "tutorials_finished": [
                    "unlocking_germany_1",
                    "unlocking_germany_2",
                    "unlocking_germany_0",
                    "germany_cards_rewarded",
                    "unlocking_usa_8",
                    "recruit_missions_done",
                    "draft_1",
                    "draft_ally",
                    "draft_kredits",
                    "unlocking_japan_0",
                    "japan_cards_rewarded",
                    "unlocking_soviet_0",
                    "soviet_cards_rewarded",
                    "unlocking_usa_0",
                    "usa_cards_rewarded",
                    "unlocking_britain_0",
                    "britain_cards_rewarded"
                ],
                "usa_level": 500,
                "usa_level_claimed": 500,
                "usa_xp": 0,
                "user_id": ID
            }

            resp.media = data
            resp.status = falcon.HTTP_200
        except Exception as e:
            print(e)