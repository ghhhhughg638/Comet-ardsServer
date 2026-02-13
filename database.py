# database.py
from typing import Optional

from tortoise import Tortoise, run_async
from models import User, Decks
from config import DATABASE_URL


class DatabaseManager:
    """状态管理器，记录数据库的基本状态"""

    def __init__(self):
        """
        状态管理器，记录数据库的基本状态
        :param self.db_url 是MySQL数据库的连接地址
        :param self._initialized 是连接数据库是否成功的结果
        """
        self.deck = None
        self.user = None
        self.db_url: str | None = None
        self._initialized: bool = False

    async def initialize(self, db_url: str = DATABASE_URL) -> bool:  #连接
        """
        连接数据库
        连接数据库的方法
        :param db_url:进行连接的MySQL数据库地址
        :return: bool 连接是否成功
        """
        self.db_url = db_url

        try:
            await Tortoise.init(
                db_url=self.db_url,
                modules={'models': ['models']}
            )
            self._initialized: bool = True
            print("✅ 数据库连接成功")
            return True
        except Exception as e:
            print(f"❌ 数据库连接失败: {e}")
            return False

    async def create_tables(self) -> bool:
        """
        检查及创建表
        检查数据库中的各个表是否存在
        :return: bool 检查是否通过
        """
        if not self._initialized:
            return False
        import warnings
        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.filterwarnings('ignore', message="Table '.*' already exists")
            await Tortoise.generate_schemas()
        for warning in caught_warnings:
            if "already exists" in str(warning.message):
                print("ℹ️  表已存在，无需创建")
                break
            else:
                print("✅ 表创建成功")
                break
        print("✅ 表结构检查完成")
        return True

    async def Find_user_data(self, list_name: str, data: str) -> Optional[User]:
        """
        查找用户数据
        通过users表中的主要不重复列查找唯一的用户数据
        :param list_name: 查找的数据的列名
        :param data: 查找的数据的内容
        :return: User用户的对象，从中得到数据
        """
        self.user = await User.get(**{list_name: data})
        return self.user

    async def Check_User_Presence(self, **filters) -> bool:
        """
        检查用户是否存在
        格式:username = "Username1"
        username: str, password: str,JWT:str
        :param filters: 为解包参数，希望传入的username,password,JWT
        :return: 返回存在性bool
        """
        if not self._initialized:
            await self.initialize()

        exists = await User.filter(**filters).exists()
        print(f"🔍 用户存在检查: {filters} -> {exists}")
        return exists

    async def Check_Deck_Presence(self, **filters) -> bool:
        """
        检查卡组是否存在
        格式:id = 1
        id: int
        :param filters: 为解包的参数，希望传入的id
        :return: 返回存在性bool
        """
        if not self._initialized:
            await self.initialize()

        exists = await Decks.filter(**filters).exists()
        print(f"🔍 卡组存在检查: {filters} -> {exists}")
        return exists

    async def Find_Deck_data(self, list_name: str, data: str) -> Optional[Decks]:
        """
        查找用户数据
        通过decks表中的主要不重复列查找唯一的用户数据
        :param list_name: 查找的数据的列名
        :param data: 查找的数据的内容
        :return: Deck用户的对象，从中得到数据
        """
        self.deck = await Decks.get(**{list_name: data})
        return self.deck

    async def Create_New_User(self, username: str, password: str) -> Optional[User]:
        """
        创建新用户
        :param username:用户的username作为独一无二的设备标识,必填选项,
        :param password:用户的password作为验证的密码,防止冒名登录
        :return:返回User对象,进行操作
        """
        try:
            user = await User.create(
                username=username,
                password=password,
                player_name="<anon>",
                player_tag=0000,
                player_JWT=""
            )
            print(f"✅ 用户创建成功: {username}")
            return user
        except Exception as e:
            print(f"❌ 创建用户失败: {e}")
            return None

    async def Create_New_Deck(self,deck:dict,user:User):
        """
        创建新卡组
        :param user: 传入的数据库对象，用于创建属于该用于的卡组
        :param deck: 卡组信息，创建的卡组的国家等信息
        :return: 返回Deck对象，进行操作
        """
        try:
            new_deck = await Decks.create(
                name=deck.get('name'),
                main_faction=deck.get('main_faction'),
                ally_faction=deck.get('ally_faction'),
                deck_code=deck.get('deck_code'),
                favorite=False,
                card_back='',
                last_played=deck.get('last_played'),
                create_date=deck.get('create_date'),
                modify_date=deck.get('modify_date'),
                user=user
            )
            print("✅ 创建卡组成功")
            return new_deck
        except Exception as e:
            print(f'❌ 创建卡组失败{e}')


db = DatabaseManager()
