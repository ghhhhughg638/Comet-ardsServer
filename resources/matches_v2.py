import json
import random

import falcon
from falcon import HTTPUnauthorized, Request, Response

from database import db, User, Decks
from websocket import server
from config import host, port
from timez import Timez_Create_Now
from deck_manager import deck_manager_ex


class MatchesV2Resource:
    async def on_get(self, req: Request, resp: Response):
        try:
            user: User = req.context.user
            if user.id in server.playing_queue:
                match_id: int = server.playing_queue[user.id]
                match_data: dict = server.match.get(match_id)
                left_deck_code = await db.Find_Deck_data(list_name="id", data=match_data.get('deck_id_left'))
                right_deck_code = await db.Find_Deck_data(list_name="id", data=match_data.get('deck_id_right'))
                left_deck_data = deck_manager_ex.parse_deck_code(deck_code=left_deck_code.deck_code)
                left_cards_data = deck_manager_ex.create_match_cards(player_way='left', deck_data=left_deck_data)
                left_hp = left_cards_data[0]
                del left_cards_data[0]
                random.shuffle(left_cards_data)
                for num, value in enumerate(left_cards_data): left_cards_data[num]['location_number'] = num
                right_deck_data = deck_manager_ex.parse_deck_code(deck_code=right_deck_code.deck_code)
                right_cards_data = deck_manager_ex.create_match_cards(player_way='right', deck_data=right_deck_data)
                right_hp = right_cards_data[0]
                del right_cards_data[0]
                random.shuffle(right_cards_data)
                for num, value in enumerate(right_cards_data): right_cards_data[num]['location_number'] = num
                resp.media = {
                    "local_subactions": True,  # 是否启用本地子动作处理
                    "match_and_starting_data": {
                        "match": {
                            "action_player_id": match_data.get('player_left'),  # 左侧玩家
                            "action_side": "left",
                            "actions": match_data.get('actions'),  # 动作历史记录
                            "actions_url": f"http://{host}:{port}/matches/v2/{match_data.get('player_left')}/actions",
                            # 左侧玩家动作API
                            "current_action_id": match_data.get('current_action_id'),  # 当前动作ID
                            "current_turn": match_data.get('current_turn'),  # 当前回合数
                            "deck_id_left": match_data.get('deck_id_left'),  # 左侧玩家卡组ID
                            "deck_id_right": match_data.get('deck_id_right'),  # 右侧玩家卡组ID
                            "left_is_online": match_data.get('left_is_online'),  # 左侧玩家是否在线
                            "match_id": match_id,  # 比赛ID
                            "match_type": match_data.get('match_type'),  # 比赛类型对战
                            "match_url": f"http://{host}:{port}/matches/v2/{match_data.get('player_right')}",  # 左侧玩家的比赛API
                            "modify_date": json.dumps(await Timez_Create_Now()),  # 比赛最后修改时间
                            "notifications": match_data.get('notifications'),  # 通知列表
                            "player_id_left": match_data.get('player_left'),  # 左侧玩家ID
                            "player_id_right": match_data.get('player_right'),  # 右侧玩家ID
                            "player_status_left": match_data.get('player_status_left'),  # 等待左侧玩家开局换牌完成
                            "player_status_right": match_data.get('player_status_right'),  # 等待右侧开局换牌完成
                            "right_is_online": match_data.get('right_is_online'),  # 右侧玩家是否在线
                            "start_side": "left",  # 先手玩家
                            "status": match_data.get('status'),  # 比赛状态，pending等待中
                            "winner_id": match_data.get('winner_id'),  # 胜利者,0表示无
                            "winner_side": match_data.get('winner_side')  # 胜利方,空字符串表示无
                        },
                        "starting_data": {  # 游戏起始数据
                            "ally_faction_left": left_deck_data.get('ally_country'),  # 左侧玩家的盟国,poland波兰
                            "ally_faction_right": right_deck_data.get('ally_country'),  # 右侧玩家的盟国,italy意大利
                            "card_back_left": "cardback_1st_tank_regiment",  # 左侧玩家卡背样式
                            "card_back_right": "cardback_11_infantry",  # 右侧玩家卡背样式
                            "starting_hand_left": left_cards_data[:4],
                            "starting_hand_right": right_cards_data[:5],
                            "deck_left": left_cards_data[4:],
                            "deck_right": right_cards_data[5:],
                            "equipment_left": [  # 左侧玩家装备/表情/头像等
                                "item_lugerinn",  # 桌饰，不知道啥
                                "emote_christmas_ho_ho_ho",  # 表情
                                "emote_honorable_fight",  # 表情
                                "emote_that_was_enlightening",  # 表情
                                "emote_boo",  # 表情，
                                "emote_glory_empire",  # 表情
                                "avatar_white_death",  # 头像
                                "emote_show_me_new"  # 表情
                            ],
                            "equipment_right": [
                                "item_lugerinn",
                                "emote_glhf",
                                "emote_its_over",
                                "emote_watch_me",
                                "emote_sorry",
                                "emote_boo",
                                "emote_achtung",
                                "emote_nuts",
                                "avatar_2e_brigade"  # 头像，其余是表情，第一个是手枪
                            ],
                            "is_ai_match": False,  # 是否是AI对战
                            "left_player_name": 'left',  # 左侧玩家名称
                            "left_player_officer": False,  # 左侧玩家是否是军官俱乐部
                            "left_player_tag": 0000,  # 左侧玩家的标签
                            "location_card_left": left_hp,
                            "location_card_right": right_hp,
                            "player_id_left": match_data.get('player_left'),
                            "player_id_right": match_data.get('player_right'),
                            "player_stars_left": 20,  # 左侧玩家的段位星数
                            "player_stars_right": 20,  # 右侧玩家的额段位星数
                            "right_player_name": 'right',  # 右侧玩家的名称
                            "right_player_officer": False,
                            "right_player_tag": 0000
                        }
                    },
                    "action_player_id": match_data.get('player_right'),
                    "action_side": "right"
                }
            elif user.id in server.waiting_queue:
                resp.media = 'null'
        except Exception as e:
            print(e)