import json

from deck_code_library import deckCodeIDsTable


class deck_manager:
    def parse_deck_code(self, deck_code: str):
        """
        解析KARDS卡组代码（增强版：处理波浪号和总部）

        参数:
            deck_code: 卡组代码，格式如 "%%46|8C;7R;;7H848b8NiQjtnrrVt9~8C;7R;;7H848b8NiQjtnrrVt9|8v1i"

        返回:
            {
                "success": True/False,
                "main_country": "德国",
                "ally_country": "日本",
                "import_ids": {"oT": 1, "40": 1, ...},  # importId: 数量
                "total_cards": 39,
                "unique_cards": 20,
                "error": "错误信息"  # 仅当success=False时存在
            }
        """
        # 国家代码映射
        COUNTRY_MAP = {
            "1": "Germany", "2": "Britain", "3": "Japan",
            "4": "Soviet", "5": "USA", "6": "France",
            "7": "Italy", "8": "Poland", "9": "Finland"
        }

        try:
            # 验证格式
            if not deck_code.startswith("%%"):
                return {"success": False, "error": "卡组代码必须以 %% 开头"}

            # 提取国家部分
            code_without_prefix = deck_code[2:]  # 移除 %%

            if "|" not in code_without_prefix:
                return {"success": False, "error": "卡组代码格式错误，缺少 | 分隔符"}

            # 分割所有部分（现在可能有3部分：国家|卡牌|总部）
            parts = code_without_prefix.split("|")

            # 判断是否有总部部分
            if len(parts) == 3:
                # 格式: 国家|卡牌|总部
                country_part, cards_part, hq_part = parts
                hq_code = hq_part
                print(f"检测到总部代码: {hq_code}")
            elif len(parts) == 2:
                # 格式: 国家|卡牌 (无总部)
                country_part, cards_part = parts
                hq_code = None
            else:
                return {"success": False, "error": f"卡组代码格式不正确，应有2或3部分，实际有{len(parts)}部分"}

            # 解析国家
            if len(country_part) != 2:
                return {"success": False, "error": f"国家代码长度不正确: {country_part}"}

            main_code = country_part[0]
            ally_code = country_part[1]

            main_country = COUNTRY_MAP.get(main_code, f"未知({main_code})")
            ally_country = COUNTRY_MAP.get(ally_code, f"未知({ally_code})")

            # 处理卡牌部分的波浪号问题
            print(f"原始卡牌部分: {cards_part}")

            if "~" in cards_part:
                print(f"检测到波浪号 ~，处理重复部分")
                # 分割波浪号前后的部分
                before_wave, after_wave = cards_part.split("~", 1)
                print(f"波浪号前: {before_wave}")
                print(f"波浪号后: {after_wave}")

                # 检查是否是重复的（通常波浪号后的部分是重复的）
                if before_wave == after_wave:
                    print(f"两部分相同，使用前部分")
                    cards_part = before_wave
                else:
                    # 如果不完全相同，使用前部分并警告
                    print(f"警告: 波浪号前后部分不完全相同")
                    print(f"  使用前部分: {before_wave}")
                    print(f"  忽略后部分: {after_wave}")
                    cards_part = before_wave

            # 分割卡牌分组（应该是4组）
            card_groups = cards_part.split(";")

            if len(card_groups) != 4:
                return {"success": False, "error": f"卡牌分组数量应为4组，实际得到{len(card_groups)}组"}

            # 解码卡牌（每组2个字符一张卡）
            # 每个分组的倍率：第1组x1，第2组x2，第3组x3，第4组x4
            group_multipliers = [1, 2, 3, 4]

            import_id_counts = {}

            for i, group in enumerate(card_groups):
                if not group:  # 空组跳过
                    continue

                # 每2个字符一个importId
                for j in range(0, len(group), 2):
                    if j + 1 < len(group):
                        import_id = group[j:j + 2]
                        count = group_multipliers[i]

                        # 累加数量
                        if import_id in import_id_counts:
                            import_id_counts[import_id] += count
                        else:
                            import_id_counts[import_id] = count

            # 计算总卡牌数
            total_cards = sum(import_id_counts.values())
            unique_cards = len(import_id_counts)

            # 构建返回结果（保持原有格式）
            result = {
                "success": True,
                "main_country": main_country,
                "ally_country": ally_country,
                "import_ids": import_id_counts,
                "total_cards": total_cards,
                "unique_cards": unique_cards,
                "deck_code": deck_code
            }

            # 如果有总部代码，添加到结果中
            if hq_code:
                result["hq_code"] = hq_code
            print(result)
            return result

        except Exception as e:
            return {"success": False, "error": f"解析过程中发生错误: {str(e)}"}

    def create_match_cards(self, player_way: str, deck_data: dict):
        main_country: str = deck_data.get('main_country')
        ally_country: str = deck_data.get('ally_country')
        hq_code: str = deck_data.get('hq_code')[:2]
        import_ids: dict = deck_data.get('import_ids')
        deck_list = []
        if player_way == 'left':
            deck_list.append(
                {  # 左侧玩家支援阵线的卡(总部)
                    "card_id": 1,
                    "faction": main_country,
                    "is_gold": True,
                    "location": "board_hqleft",  # 位置左侧总部
                    "location_number": 0,
                    "name": deckCodeIDsTable.get(hq_code).get('card')
                }
            )
            card_id = 2
            location = 'deck_left'

        elif player_way == 'right':
            deck_list.append(
                {  # 右侧玩家支援阵线的卡(总部)
                    "card_id": 41,
                    "faction": main_country,
                    "is_gold": True,
                    "location": "board_hqright",  # 位置左侧总部
                    "location_number": 0,
                    "name": deckCodeIDsTable.get(hq_code).get('card')
                }
            )
            card_id = 42
            location = 'deck_right'
        location_num = 0
        for deck, num in import_ids.items():
            for i in range(num):
                deck_list.append(
                    {
                        "card_id": card_id,
                        "is_gold": True,
                        "location": location,
                        "location_number": location_num,
                        "name": deckCodeIDsTable.get(deck).get('card')
                    }
                )
                card_id += 1
                location_num += 1

        return deck_list


deck_manager_ex = deck_manager()

