from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)  # 主键字段，表示每一行数据的唯一标识
    username = fields.CharField(max_length=50, unique=True)  # 用户名，最大长度50，且唯一
    password = fields.CharField(max_length=50)
    player_name = fields.CharField(max_length=50)
    player_JWT = fields.CharField(max_length=500)
    player_tag = fields.IntField(null=True)
    decks: fields.ReverseRelation["Decks"]  #设置一对多关系

    britain_level = fields.IntField(default=500)  #英国国家等级
    britain_level_claimed = fields.IntField(default=500)  #英国已经领取的国家等级奖励
    britain_xp = fields.IntField(default=0)  #英国当前级拥有的经验数

    germany_level = fields.IntField(default=500)  #德国国家等级
    germany_level_claimed = fields.IntField(default=500)  #德国已经领取的国家等级奖励
    germany_xp = fields.IntField(default=0)  #德国当前拥有的经验数

    japan_level = fields.IntField(default=500)  #日本国家等级
    japan_level_claimed = fields.IntField(default=500)  #日本已经领取的国家等级奖励
    japan_xp = fields.IntField(default=0)  #日本当前拥有的经验数

    soviet_level = fields.IntField(default=500)  #苏联国家等级
    soviet_level_claimed = fields.IntField(default=500)  #苏联已经领取的国家等级奖励
    soviet_xp = fields.IntField(default=0)  #苏联当前拥有的经验数

    usa_level = fields.IntField(default=500)  #美国国家等级
    usa_level_claimed = fields.IntField(default=500)  #美国已经领取的国家等级奖励
    usa_xp = fields.IntField(default=0)  #美国当前拥有的经验数

    claimable_crate_level = fields.IntField(default=0)  #军需箱等级
    diamonds = fields.IntField(default=0)  #钻石数量
    gold = fields.IntField(default=0)  #金币数量
    double_xp_end_date = fields.CharField(max_length=50, null=True)  #医疗包到期时间
    draft_admissions = fields.IntField(default=0)  #竞技场入场卷

    has_been_officer = fields.BooleanField(default=False)  #曾经是否是元帅
    is_officer = fields.BooleanField(default=False)  #目前是否是元帅
    season_wins = fields.IntField(default=0)  #本赛季胜场数
    stars = fields.IntField(default=0)  #当前段位星数

    is_online = fields.BooleanField(default=False)  #是否在线
    online_flag = fields.BooleanField(default=False)  #是否显示在线

    last_logon_date = fields.CharField(max_length=50, default="")  #上次登录的日期
    npc = fields.BooleanField(default=False)  #是否是npc账号

    email = fields.CharField(max_length=50, default="")  #邮箱
    email_reward_received = fields.BooleanField(default=False)  #是否领取邮箱奖励
    email_verified = fields.BooleanField(default=False)  #是否进行邮箱验证

    extended_rewards = fields.BooleanField(default=False)  #是否购买战役通行证

    created_at = fields.DatetimeField(auto_now_add=True)  # 自动记录用户创建时间

    class Meta:
        table = "user"  # 指定数据库表名
        unique_together = (("player_name", "player_tag"),)  # 复合唯一约束
        indexes = [
            "username",
            "password",
            "player_name",
            "player_tag"
        ]

        ordering = ["-created_at"]  # 按创建时间降序排列


class Decks(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20, default="")  #卡组名
    card_back = fields.CharField(max_length=50, default="")  #卡背

    main_faction = fields.CharField(max_length=20, default="")  #主国
    ally_faction = fields.CharField(max_length=20, default="")  #盟国

    deck_code = fields.CharField(max_length=250, default="")  #卡组代码
    favorite = fields.BooleanField(default=False)  #是否收藏
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        'models.User', related_name='decks', on_delete=fields.CASCADE)  #属于哪个玩家

    last_played = fields.CharField(max_length=50, default='')  # 最后使用时间
    create_date = fields.CharField(max_length=50, default='')  # 创建时间
    modify_date = fields.CharField(max_length=50, default='')  # 修改时间

    class Meta:
        table = "decks"
