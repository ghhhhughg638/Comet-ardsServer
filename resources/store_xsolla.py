import falcon
import falcon.asgi


class XsollaResource:
    async def on_get(self, req, resp):
        resp.media = {
            "alwaysFeatured": {
                "endDate": "2099-01-01T00:00:00Z",
                "group": 1,
                "groupId": -1,
                "offers": [
                    {
                        "description": "魔理沙写真集x1",
                        "diamonds": 91,
                        "items": [
                            {
                                "data": {
                                    "cardCount": 7,
                                    "cardSet": "BrothersInArms",
                                    "guaranteedGoldCards": 0,
                                    "itemType": "pack"
                                },
                                "qty": 30
                            }
                        ],
                        "limit": 10,
                        "mainImage": "https://i0.hdslb.com/bfs/new_dyn/84b519d8035b05a63c82678651e42a1b316571441.jpg",
                        "offerId": 6796213,
                        "offerName": "offer_30_officer_packs_-_naval_warfare_live",
                        "priority": 5,
                        "thumbnail": "https://i0.hdslb.com/bfs/new_dyn/84b519d8035b05a63c82678651e42a1b316571441.jpg",
                        "title": "魔理沙写真集"
                    },
                    {
                        "description": "看到的请祝我们99",
                        "diamonds": 52321,
                        "items": [
                            {
                                "data": {
                                    "cardCount": 7,
                                    "cardSet": "Core",
                                    "guaranteedGoldCards": 0,
                                    "itemType": "pack"
                                },
                                "qty": 30
                            }
                        ],
                        "mainImage": "https://i0.hdslb.com/bfs/archive/1868996d4869cecd6e904ae5827a9d3c569f877d.jpg",
                        "offerId": 6777130,
                        "offerName": "offer_30_core_officer_packs_backup_offer",
                        "priority": 7,
                        "thumbnail": "https://i0.hdslb.com/bfs/archive/1868996d4869cecd6e904ae5827a9d3c569f877d.jpg",
                        "title": "abby&larkord1st"
                    },
                    {
                        "description": "每个卡包内含：\n• 7 张海战卡牌\n• 至少 2 张限定或更高稀有度卡牌\n• 至少 1 张特殊或精英卡牌\n• 有几率掉落万能牌和闪卡\n\n海战，KARDS 第 9 个大型扩展包，引入了 87 张全新卡牌以及来自预备卡池的一系列回归卡牌。本次扩展包深入海上冲突的核心，将史诗级的海战与军舰推向舞台中心。海战首次推出海军子类型以及创新转换机制，开辟新的战术选择与强力组合。迎接 KARDS 历史上最为刺激、最具深度的新篇章，统领大海！",
                        "diamonds": 850,
                        "items": [
                            {
                                "data": {
                                    "cardCount": 7,
                                    "cardSet": "NavalWarfare",
                                    "guaranteedGoldCards": 0,
                                    "itemType": "pack"
                                },
                                "qty": 20
                            }
                        ],
                        "limit": 0,
                        "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_20_officer_packs___naval_warfare/navalwarfare_20_officer_1280x720.jpg",
                        "offerId": 6798220,
                        "offerName": "offer_20_officer_packs_-_naval_warfare",
                        "priority": 8,
                        "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_20_officer_packs___naval_warfare/navalwarfare_20_officer_1280x720.jpg",
                        "title": "20 个军官卡包 - 海战"
                    }
                ],
                "startDate": "2018-01-01T00:00:00Z"
            },
            "currency": "USD",
            "groups": [
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 5,
                    "groupId": 27,
                    "offers": [
                        {
                            "bonusItems": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 10
                                }
                            ],
                            "description": "钻石可以用于在商店中购买卡包、捆绑包特惠和装备。",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 48
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_s/diamond_bundle1_parcel_productimage02.jpg",
                            "offerId": 16566,
                            "offerName": "diamonds_s",
                            "real": 4.99,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/ShopAssetsPlusThumbs/Diamond_offers_10_03_2022/diamond_bundle1_parcel_thumb.png",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_s/diamond_bundle1_parcel_thumb02.jpg",
                            "title": "48钻石"
                        }
                    ],
                    "startDate": "2023-04-19T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 73,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 5 张核心卡牌\n• 至少 1 张限定或更高稀有度卡牌\n\n核心卡包包含您起步所需的全部卡牌。核心卡池收录了所有主国（德国、英国、苏联、美国和日本）以及所有盟国（法国、意大利、波兰和芬兰）的卡牌。",
                            "diamonds": 14,
                            "gold": 100,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_1_core_pack/core_packs_1_lowres2.jpg",
                            "offerId": 16569,
                            "offerName": "offer_1_core_pack",
                            "slotType": "most_popular",
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_1_core_pack/core_packs_1.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_1_core_pack/core_packs_officer_20_lowres2.jpg",
                            "title": "1个卡包 - 核心套装"
                        }
                    ],
                    "startDate": "2023-05-06T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 5,
                    "groupId": 74,
                    "offers": [
                        {
                            "bonusItems": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 30
                                }
                            ],
                            "description": "一盒钻石内含100颗钻石。钻石可以用于在商店中购买卡包、捆绑包特惠和装备。",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 100
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_m/diamond_bundle2_matchbox_productimage02.jpg",
                            "offerId": 16928,
                            "offerName": "diamonds_m",
                            "real": 9.99,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/ShopAssetsPlusThumbs/Diamond_offers_10_03_2022/diamond_bundle2_matchbox_thumb.png",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_m/diamond_bundle2_matchbox_thumb02.jpg",
                            "title": "100钻石"
                        }
                    ],
                    "startDate": "2023-05-06T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 5,
                    "groupId": 75,
                    "offers": [
                        {
                            "bonusItems": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 75
                                }
                            ],
                            "description": "一包钻石内含210颗钻石。钻石可以用于在商店中购买卡包、捆绑包特惠和装备。",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 210
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_l/diamond_bundle3_leatherbag_productimage02.jpg",
                            "offerId": 16929,
                            "offerName": "diamonds_l",
                            "real": 19.99,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/ShopAssetsPlusThumbs/Diamond_offers_10_03_2022/diamond_bundle3_leatherBag_thumb.png",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_l/diamond_bundle3_leatherbag_thumb02.jpg",
                            "title": "210钻石"
                        }
                    ],
                    "startDate": "2023-05-06T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 5,
                    "groupId": 76,
                    "offers": [
                        {
                            "bonusItems": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 155
                                }
                            ],
                            "description": "一杯钻石具有优惠，内含380颗钻石。钻石可以用于在商店中购买卡包、捆绑包特惠和装备。",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 380
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_xl/diamond_bundle4_cup_productimage02.jpg",
                            "offerId": 16930,
                            "offerName": "diamonds_xl",
                            "real": 34.99,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/ShopAssetsPlusThumbs/Diamond_offers_10_03_2022/diamond_bundle4_Cup_thumb.png",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_xl/diamond_bundle4_cup_thumb02.jpg",
                            "title": "380钻石"
                        }
                    ],
                    "startDate": "2023-05-06T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 5,
                    "groupId": 77,
                    "offers": [
                        {
                            "bonusItems": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 260
                                }
                            ],
                            "description": "一帽钻石非常合算，内含570颗钻石。钻石可以用于在商店中购买卡包、捆绑包特惠和装备。",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 570
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_xxl/diamond_bundle5_helmet_productimage02.jpg",
                            "offerId": 16931,
                            "offerName": "diamonds_xxl",
                            "real": 49.99,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/ShopAssetsPlusThumbs/Diamond_offers_10_03_2022/diamond_bundle5_helmet_thumb.png",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_xxl/diamond_bundle5_helmet_thumb02.jpg",
                            "title": "570钻石"
                        }
                    ],
                    "startDate": "2023-05-06T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 5,
                    "groupId": 78,
                    "offers": [
                        {
                            "bonusItems": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 600
                                }
                            ],
                            "description": "一箱钻石具有大幅优惠，内含1200颗钻石。钻石可以用于在商店中购买卡包、捆绑包特惠和装备。",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 1200
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_xxxl/diamond_bundle6_chest_productimage02.jpg",
                            "offerId": 16932,
                            "offerName": "diamonds_xxxl",
                            "real": 99.99,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/ShopAssetsPlusThumbs/Diamond_offers_10_03_2022/diamond_bundle6_chest_thumb.png",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/diamonds_xxxl/diamond_bundle6_chest_thumb02.jpg",
                            "title": "1200钻石"
                        }
                    ],
                    "startDate": "2023-05-06T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 80,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 5 张核心卡牌\n• 至少 1 张限定或更高稀有度卡牌\n\n核心卡包包含您起步所需的全部卡牌。核心卡池收录了所有主国（德国、英国、苏联、美国和日本）以及所有盟国（法国、意大利、波兰和芬兰）的卡牌。",
                            "diamonds": 98,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 7
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_packs/core_packs_7_lowres2.jpg",
                            "offerId": 16962,
                            "offerName": "packs_7_packs",
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_packs/core_packs_7.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_packs/core_packs_7_lowres2.jpg",
                            "title": "7个卡包 - 核心套装"
                        }
                    ],
                    "startDate": "2023-05-08T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 86,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 7 张核心卡牌\n• 至少 2 张限定或更高稀有度卡牌\n• 至少 1 张特殊或精英卡牌\n• 可能掉落万能牌和闪卡\n\n核心卡包包含您起步所需的全部卡牌。核心卡池收录了所有主国（德国、英国、苏联、美国和日本）以及所有盟国（法国、意大利、波兰和芬兰）的卡牌。军官卡包内含更多卡牌和更高稀有度的卡牌。",
                            "diamonds": 43,
                            "gold": 330,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_1_officer_pack___core/core_packs_officer_1_lowres2.jpg",
                            "offerId": 16974,
                            "offerName": "packs_1_officer_pack_-_core",
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_1_officer_pack_-_core/core_packs_officer_1.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_1_officer_pack___core/core_packs_officer_1_lowres2.jpg",
                            "title": "1个军官卡包 - 核心套装"
                        }
                    ],
                    "startDate": "2023-05-09T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 90,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 7 张核心卡牌\n• 至少 2 张限定或更高稀有度卡牌\n• 至少 1 张特殊或精英卡牌\n• 可能掉落万能牌和闪卡\n\n核心卡包包含您起步所需的全部卡牌。核心卡池收录了所有主国（德国、英国、苏联、美国和日本）以及所有盟国（法国、意大利、波兰和芬兰）的卡牌。军官卡包内含更多卡牌和更高稀有度的卡牌。",
                            "diamonds": 850,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 20
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_officer_packs___core/core_packs_officer_20_full_image_lowres.jpg",
                            "offerId": 16975,
                            "offerName": "packs_20_officer_packs_-_core",
                            "priority": 1002,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_officer_packs_-_core/core_packs_officer_20_v2.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_officer_packs___core/core_packs_officer_20_lowres2.jpg",
                            "title": "20个军官卡包 - 核心套装"
                        }
                    ],
                    "startDate": "2023-05-09T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 91,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 7 张核心卡牌\n• 至少 2 张限定或更高稀有度卡牌\n• 至少 1 张特殊或精英卡牌\n• 可能掉落万能牌和闪卡\n\n核心卡包包含您起步所需的全部卡牌。核心卡池收录了所有主国（德国、英国、苏联、美国和日本）以及所有盟国（法国、意大利、波兰和芬兰）的卡牌。军官卡包内含更多卡牌和更高稀有度的卡牌。",
                            "diamonds": 300,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 7
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_officer_packs___core/core_packs_officer_7_lowres2.jpg",
                            "offerId": 16973,
                            "offerName": "packs_7_officer_packs_-_core",
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_officer_packs_-_core/core_packs_officer_7.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_officer_packs___core/core_packs_officer_7_lowres2.jpg",
                            "title": "7个军官卡包 - 核心套装"
                        }
                    ],
                    "startDate": "2023-05-09T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 92,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 5 张核心卡牌\n• 至少 1 张限定或更高稀有度卡牌\n\n核心卡包包含您起步所需的全部卡牌。核心卡池收录了所有主国（德国、英国、苏联、美国和日本）以及所有盟国（法国、意大利、波兰和芬兰）的卡牌。",
                            "diamonds": 280,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 20
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_packs___core/core_packs_20_lowres2.jpg",
                            "offerId": 16971,
                            "offerName": "packs_20_packs_-_core",
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_packs_-_core/core_packs_20.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_packs___core/core_packs_20_lowres2.jpg",
                            "title": "20个卡包 - 核心套装"
                        }
                    ],
                    "startDate": "2023-05-09T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 1,
                    "groupId": 157,
                    "offers": [],
                    "startDate": "2023-06-08T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 11,
                    "groupId": 1198,
                    "hidden": True,
                    "offers": [
                        {
                            "description": "战区引入了五个单人 PVE 战役，在不同的历史场景中进行，你将在危机四伏的环境中接受特殊的任务目标，不断挑战技能和决心。战区包括以下 5 个历史战役：莫斯科保卫战（苏联）、第二次阿拉曼战役（德国）、菲律宾战役（日本）、瓜达尔卡纳尔岛战役（美国）和突尼斯战役（英国）。\n\n完成战役以获得战区国家卡背，每个国家一张。在战役中获得满星，可为每个国家解锁一个特殊表情。",
                            "diamonds": 148,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "campaign",
                                        "name": "campaign_britain1"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "campaign",
                                        "name": "campaign_germany1"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "campaign",
                                        "name": "campaign_soviet1"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "campaign",
                                        "name": "campaign_japan1"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "campaign",
                                        "name": "campaign_us1"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/campaigns_theaters_of_war/store-tow_campaign_thumbcn.jpg",
                            "offerId": 6757643,
                            "offerName": "campaigns_theaters_of_war",
                            "priority": 50,
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/campaigns_theaters_of_war/store-tow_campaign_thumbcn.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/campaigns_theaters_of_war/store-tow_campaign_thumbcn.jpg",
                            "title": "战区"
                        }
                    ],
                    "startDate": "2024-08-28T10:54:00Z"
                },
                {
                    "endDate": "2030-03-12T11:00:00Z",
                    "group": 1,
                    "groupId": 1796,
                    "offers": [],
                    "startDate": "2025-03-12T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 7,
                    "groupId": 1814,
                    "offers": [
                        {
                            "description": "Battle Pass 3 Months",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "token",
                                        "name": "token_3_month_pass"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6789284,
                            "offerName": "multiple_battle_passes_-_3_months",
                            "real": 31.99,
                            "title": "Battle Pass 3 Months"
                        }
                    ],
                    "startDate": "2025-03-20T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 7,
                    "groupId": 1815,
                    "offers": [
                        {
                            "description": "Battle Pass 6 Months",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "token",
                                        "name": "token_6_month_pass"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6789285,
                            "offerName": "multiple_battle_passes_-_6_months",
                            "real": 59.99,
                            "title": "Battle Pass 6 Months"
                        }
                    ],
                    "startDate": "2025-03-20T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 2219,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 7 张海战卡牌\n• 至少 2 张限定或更高稀有度卡牌\n• 至少 1 张特殊或精英卡牌\n• 有几率掉落万能牌和闪卡\n\n海战，KARDS 第 9 个大型扩展包，引入了 87 张全新卡牌以及来自预备卡池的一系列回归卡牌。本次扩展包深入海上冲突的核心，将史诗级的海战与军舰推向舞台中心。海战首次推出海军子类型以及创新转换机制，开辟新的战术选择与强力组合。迎接 KARDS 历史上最为刺激、最具深度的新篇章，统领大海！",
                            "diamonds": 43,
                            "gold": 330,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "NavalWarfare",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_1_officer_pack___naval_warfare/navalwarfare_1_officer_1280x720.jpg",
                            "offerId": 6796209,
                            "offerName": "packs_1_officer_pack_-_naval_warfare",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_1_officer_pack___naval_warfare/navalwarfare_20_officer_1280x720.jpg",
                            "title": "1 个军官卡包 - 海战"
                        }
                    ],
                    "startDate": "2025-06-18T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 2221,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 7 张海战卡牌\n• 至少 2 张限定或更高稀有度卡牌\n• 至少 1 张特殊或精英卡牌\n• 有几率掉落万能牌和闪卡\n\n海战，KARDS 第 9 个大型扩展包，引入了 87 张全新卡牌以及来自预备卡池的一系列回归卡牌。本次扩展包深入海上冲突的核心，将史诗级的海战与军舰推向舞台中心。海战首次推出海军子类型以及创新转换机制，开辟新的战术选择与强力组合。迎接 KARDS 历史上最为刺激、最具深度的新篇章，统领大海！",
                            "diamonds": 850,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "NavalWarfare",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 20
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_officer_packs___naval_warfare/navalwarfare_20_officer_1280x720.jpg",
                            "offerId": 6796211,
                            "offerName": "packs_20_officer_packs_-_naval_warfare",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_officer_packs___naval_warfare/navalwarfare_20_officer_1280x720.jpg",
                            "title": "20 个军官卡包 - 海战"
                        }
                    ],
                    "startDate": "2025-06-18T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 2216,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 5 张海战卡牌\n• 至少 1 张限定或更高稀有度卡牌\n\n海战，KARDS 第 9 个大型扩展包，引入了 87 张全新卡牌以及来自预备卡池的一系列回归卡牌。本次扩展包深入海上冲突的核心，将史诗级的海战与军舰推向舞台中心。海战首次推出海军子类型以及创新转换机制，开辟新的战术选择与强力组合。迎接 KARDS 历史上最为刺激、最具深度的新篇章，统领大海！",
                            "diamonds": 14,
                            "gold": 100,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "NavalWarfare",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_1_pack___naval_warfare/navalwarfare_1_regular_1280x720.jpg",
                            "offerId": 6796206,
                            "offerName": "packs_1_pack_-_naval_warfare",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_1_pack___naval_warfare/navalwarfare_20_officer_1280x720.jpg",
                            "title": "1 个卡包 - 海战"
                        }
                    ],
                    "startDate": "2025-06-18T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 2217,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 5 张海战卡牌\n• 至少 1 张限定或更高稀有度卡牌\n\n海战，KARDS 第 9 个大型扩展包，引入了 87 张全新卡牌以及来自预备卡池的一系列回归卡牌。本次扩展包深入海上冲突的核心，将史诗级的海战与军舰推向舞台中心。海战首次推出海军子类型以及创新转换机制，开辟新的战术选择与强力组合。迎接 KARDS 历史上最为刺激、最具深度的新篇章，统领大海！",
                            "diamonds": 98,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "NavalWarfare",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 7
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_packs___naval_warfare/navalwarfare_7_regular_1280x720.jpg",
                            "offerId": 6796207,
                            "offerName": "packs_7_packs_-_naval_warfare",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_packs___naval_warfare/navalwarfare_7_regular_1280x720.jpg",
                            "title": "7 个卡包 - 海战"
                        }
                    ],
                    "startDate": "2025-06-18T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 2218,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 5 张海战卡牌\n• 至少 1 张限定或更高稀有度卡牌\n\n海战，KARDS 第 9 个大型扩展包，引入了 87 张全新卡牌以及来自预备卡池的一系列回归卡牌。本次扩展包深入海上冲突的核心，将史诗级的海战与军舰推向舞台中心。海战首次推出海军子类型以及创新转换机制，开辟新的战术选择与强力组合。迎接 KARDS 历史上最为刺激、最具深度的新篇章，统领大海！",
                            "diamonds": 280,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "NavalWarfare",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 20
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_packs___naval_warfare/navalwarfare_20_regular_1280x720.jpg",
                            "offerId": 6796208,
                            "offerName": "packs_20_packs_-_naval_warfare",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_20_packs___naval_warfare/navalwarfare_20_regular_1280x720.jpg",
                            "title": "20 个卡包 - 海战"
                        }
                    ],
                    "startDate": "2025-06-18T11:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 4,
                    "groupId": 2220,
                    "offers": [
                        {
                            "description": "每个卡包内含：\n• 7 张海战卡牌\n• 至少 2 张限定或更高稀有度卡牌\n• 至少 1 张特殊或精英卡牌\n• 有几率掉落万能牌和闪卡\n\n海战，KARDS 第 9 个大型扩展包，引入了 87 张全新卡牌以及来自预备卡池的一系列回归卡牌。本次扩展包深入海上冲突的核心，将史诗级的海战与军舰推向舞台中心。海战首次推出海军子类型以及创新转换机制，开辟新的战术选择与强力组合。迎接 KARDS 历史上最为刺激、最具深度的新篇章，统领大海！",
                            "diamonds": 300,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "NavalWarfare",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 7
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_officer_packs___naval_warfare/navalwarfare_7_officer_1280x720.jpg",
                            "offerId": 6796210,
                            "offerName": "packs_7_officer_packs_-_naval_warfare",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/packs_7_officer_packs___naval_warfare/navalwarfare_7_officer_1280x720.jpg",
                            "title": "7 个军官卡包 - 海战"
                        }
                    ],
                    "startDate": "2025-06-18T11:00:00Z"
                },
                {
                    "endDate": "2025-09-01T00:00:00Z",
                    "group": 6,
                    "groupId": 1801,
                    "offers": [
                        {
                            "description": "Wards元旦快乐！\n元旦快乐",
                            "fulfilAfter": "2025-08-01T00:00:00Z",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "bp",
                                        "month": 8,
                                        "year": 2025
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "avatar",
                                        "name": "avatar_paratrooper"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "cardback",
                                        "name": "cardback_27th_armored_brigade"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "emote",
                                        "name": "emote_this_means_war"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_109th_combat_engineers"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://i2.hdslb.com/bfs/archive/e06ffa4b02ac5784cb2f94dda7faa6fbec5c6224.jpg",
                            "offerId": 6789282,
                            "offerName": "battle_pass_08/25",
                            "real": 12.13,
                            "thumbnail": "https://i2.hdslb.com/bfs/archive/e06ffa4b02ac5784cb2f94dda7faa6fbec5c6224.jpg",
                            "title": "Wards元旦快乐！"
                        }
                    ],
                    "startDate": "2025-08-01T00:00:00Z"
                },
                {
                    "endDate": "2025-08-25T00:00:00Z",
                    "group": 2,
                    "groupId": 2280,
                    "offers": [
                        {
                            "description": "",
                            "diamonds": 350,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "deck",
                                        "name": "deck_usa_naval_dominance"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/deck_deck_usa_naval_dominance/naval-dominance_atore.jpg",
                            "offerId": 6796778,
                            "offerName": "deck_deck_usa_naval_dominance",
                            "slotType": "",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/deck_deck_usa_naval_dominance/naval-dominance_atore.jpg",
                            "title": "海军主宰"
                        },
                        {
                            "description": "这是对现有卡牌的卡图更改，并非卡牌本身。仅会改变卡牌的视觉风格，其效果保持不变。",
                            "diamonds": 90,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_combined_arms"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6775099,
                            "offerName": "alt_art_alt_1_card_event_combined_arms",
                            "slotType": "",
                            "title": "协同作战"
                        },
                        {
                            "description": "使用交互式银元打火机个性化您的战场。该交互式打火机可以翻开盖子并旋转滑轮。该设备可用于美国卡组。",
                            "diamonds": 100,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "prop",
                                        "name": "item_Lighter_SilverDollar"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/prop_item_Lighter_SilverDollar/t_eq_us_zippo_silvercoin.png",
                            "offerId": 17161,
                            "offerName": "prop_item_Lighter_SilverDollar",
                            "slotType": "",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/prop_item_Lighter_SilverDollar/t_eq_us_zippo_silvercoin.png",
                            "title": "打火机 - 银元"
                        },
                        {
                            "description": "使用此总部来个性化您的战场，该总部会更改战场桌布。踏入热带丛林的前线。该总部可用于美国卡组。",
                            "diamonds": 100,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "card",
                                        "name": "card_location_guadalcanal"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 17204,
                            "offerName": "hq_card_location_guadalcanal",
                            "slotType": "",
                            "title": "瓜达尔卡纳尔岛"
                        },
                        {
                            "description": "德国装甲师是战争初期德国闪电战行动成功的关键因素。使用德国装甲师卡背个性化你的卡组。此卡背可用于以德国为主国的卡组。",
                            "diamonds": 30,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "cardback",
                                        "name": "cardback_panzer"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/cardback_cardback_panzer/cardback_panzer-division_product-image.jpg",
                            "offerId": 17119,
                            "offerName": "cardback_cardback_panzer",
                            "slotType": "",
                            "smallThumb": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/cardback_cardback_panzer/cardback_panzer-division_thumbnail.jpg",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/cardback_cardback_panzer/cardback_panzer-division_thumbnail.jpg",
                            "title": "德国装甲师"
                        },
                        {
                            "description": "使用这款表情个性化您的战场通信。这款欢呼表情可用于美国卡组。",
                            "diamonds": 45,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "emote",
                                        "name": "emote_splash_one_bogey"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6799197,
                            "offerName": "emote_emote_splash_one_bogey",
                            "slotType": "",
                            "title": "击落不明敌机！"
                        }
                    ],
                    "startDate": "2025-08-22T00:00:00Z"
                },
                {
                    "endDate": "2025-08-25T11:00:00Z",
                    "group": 1,
                    "groupId": 2417,
                    "offers": [
                        {
                            "description": "扎扎实已经上线wards，正在火热骑宝马中！",
                            "diamonds": 91,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 91
                                },
                                {
                                    "data": {
                                        "itemType": "diamonds"
                                    },
                                    "qty": 114514
                                },
                                {
                                    "data": {
                                        "itemType": "card",
                                        "name": "card_unit_zaza_division"
                                    },
                                    "qty": 1
                                }
                            ],
                            "limit": 2,
                            "mainImage": "https://i0.hdslb.com/bfs/new_dyn/a0984cf35756fcb09b611d1468a42f9b316571441.jpg",
                            "offerId": 6798834,
                            "offerName": "1card_unit_zaza_division",
                            "priority": 4,
                            "thumbnail": "https://i0.hdslb.com/bfs/new_dyn/a0984cf35756fcb09b611d1468a42f9b316571441.jpg",
                            "timed": True,
                            "title": "扎扎实已经上线wards，正在火热骑宝马中！"
                        }
                    ],
                    "startDate": "2025-08-22T11:00:00Z"
                },
                {
                    "endDate": "2025-08-25T11:00:00Z",
                    "group": 1,
                    "groupId": 2418,
                    "offers": [
                        {
                            "description": "买一送一,两个女仆带回家",
                            "diamonds": 98,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "Expansion2019",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 7
                                }
                            ],
                            "limit": 1,
                            "mainImage": "https://i0.hdslb.com/bfs/archive/9500568a9ca0e831c246ca1e5298d784087efe94.jpg",
                            "offerId": 6796873,
                            "offerName": "offer_7_soviet_packs_-_1_guaranteed_elite",
                            "priority": 2,
                            "thumbnail": "https://i0.hdslb.com/bfs/archive/9500568a9ca0e831c246ca1e5298d784087efe94.jpg",
                            "timed": True,
                            "title": "买一送一,两个女仆带回家"
                        }
                    ],
                    "startDate": "2025-08-22T11:00:00Z"
                },
                {
                    "endDate": "2025-09-23T11:00:00Z",
                    "group": 1,
                    "groupId": 2428,
                    "offers": [
                        {
                            "description": "咕咕嘎嘎！我说咕咕嘎嘎你二龙吗？",
                            "diamonds": 91,
                            "fulfilAfter": "2025-09-23T11:00:00Z",
                            "items": [
                                {
                                    "data": {
                                        "itemType": "token",
                                        "name": "token_name_change"
                                    },
                                    "qty": 1
                                }
                            ],
                            "limit": 0,
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_air_supremacy_pre_sales/air-supremacy_keayart_shop_2.jpg",
                            "offerId": 6799513,
                            "offerName": "offer_air_supremacy_pre-sales",
                            "priority": 1,
                            "slotType": "discount",
                            "slotValue": "55",
                            "smallThumb": "https://i0.hdslb.com/bfs/archive/0a69a137db459a481cb95925bdd7bef36c4b2a76.jpg",
                            "thumbnail": "https://i0.hdslb.com/bfs/archive/0a69a137db459a481cb95925bdd7bef36c4b2a76.jpg",
                            "timed": True,
                            "title": "咕咕嘎嘎！"
                        }
                    ],
                    "startDate": "2025-08-22T11:00:00Z"
                },
                {
                    "endDate": "2025-08-25T11:00:00Z",
                    "group": 1,
                    "groupId": 2427,
                    "offers": [
                        {
                            "description": "利用此限时优惠，助您冲击前线。",
                            "diamonds": 89,
                            "items": [
                                {
                                    "data": {
                                        "cardCount": 7,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "Core",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "cardCount": 5,
                                        "cardSet": "NavalWarfare",
                                        "guaranteedGoldCards": 0,
                                        "itemType": "pack"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "duration": 1,
                                        "itemType": "medkit"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "draft"
                                    },
                                    "qty": 1
                                }
                            ],
                            "limit": 2,
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_weekend_special___1_officer_pack_2_packs_draft_ticket_1day_medkit/kards-bundle_offer-medkit_bundle-720p.jpg",
                            "offerId": 6799572,
                            "offerName": "offer_weekend_special_-_1_officer_pack+2_packs+draft_ticket+1day_medkit",
                            "priority": 3,
                            "slotType": "most_popular",
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_weekend_special___1_officer_pack_2_packs_draft_ticket_1day_medkit/kards-bundle_offer-medkit_bundle-720p.jpg",
                            "title": "周末特惠"
                        }
                    ],
                    "startDate": "2025-08-22T11:00:00Z"
                },
                {
                    "endDate": "2025-08-24T00:00:00Z",
                    "group": 3,
                    "groupId": 2175,
                    "offers": [
                        {
                            "items": [
                                {
                                    "data": {
                                        "itemType": "card",
                                        "name": "card_unit_zaza_divison"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6715394,
                            "offerName": "card_unit_zaza_divison"
                        },
                        {
                            "bonus": True,
                            "diamonds": 8,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "card",
                                        "name": "card_unit_sturmovik_pol"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6754571,
                            "offerName": "card_unit_sturmovik_pol"
                        },
                        {
                            "diamonds": 8,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "card",
                                        "name": "card_event_sisu"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6762899,
                            "offerName": "card_event_sisu"
                        }
                    ],
                    "startDate": "2025-08-23T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 12,
                    "groupId": -1,
                    "hidden": True,
                    "offers": [
                        {
                            "diamonds": 20,
                            "gold": 150,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "draft"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6740392,
                            "offerName": "draft_ticket"
                        },
                        {
                            "diamonds": 80,
                            "items": [
                                {
                                    "data": {
                                        "duration": 7,
                                        "itemType": "medkit"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6757794,
                            "offerName": "medkit_7d"
                        },
                        {
                            "diamonds": 40,
                            "items": [
                                {
                                    "data": {
                                        "duration": 3,
                                        "itemType": "medkit"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6757793,
                            "offerName": "medkit_3d"
                        },
                        {
                            "diamonds": 20,
                            "items": [
                                {
                                    "data": {
                                        "duration": 1,
                                        "itemType": "medkit"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6757792,
                            "offerName": "medkit_1d"
                        },
                        {
                            "diamonds": 20,
                            "items": [
                                {
                                    "data": {
                                        "duration": 1,
                                        "itemType": "medkit"
                                    },
                                    "qty": 1
                                }
                            ],
                            "offerId": 6744365,
                            "offerName": "medkit"
                        }
                    ],
                    "startDate": "2018-01-01T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 1,
                    "groupId": -1,
                    "offers": [],
                    "startDate": "2018-01-01T00:00:00Z"
                },
                {
                    "endDate": "2099-01-01T00:00:00Z",
                    "group": 2,
                    "groupId": 2429,
                    "offers": [
                        {
                            "description": "包含所有异画卡牌的合集",
                            "diamonds": 10,
                            "items": [
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_amphibious_assault"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_arming_resistance"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_bloody_sickle"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_bolster_the_ranks"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_bomber_mafia"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_burning_sky"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_carpet_bombing"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_close_air_support"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_combined_arms"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_death_from_above"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_fast_heinz"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_last_rites"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_mare_nostrum"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_men_of_steel"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_mi_5"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_monty"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_naval_support"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_red_banner"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_reserves"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_rising_sun"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_tactical_strike"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_the_war_machine"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_tora_tora"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_unity_is_strength"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_ural_factories"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_event_war_bonds"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_109th_combat_engineers"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_22_infantry"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_507th_pir"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_5th_brigade"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_b_17"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_churchill"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_commandos"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_cossack_cavalry"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_fallschirmjager"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_fw_190"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_hurricane_vs2"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_p40_kittyhawk"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_p51_mustang"
                                    },
                                    "qty": 1
                                },
                                {
                                    "data": {
                                        "itemType": "alt_art",
                                        "name": "alt_1_card_unit_swordfish"
                                    },
                                    "qty": 1
                                }
                            ],
                            "mainImage": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_1_core_pack/core_packs_1_lowres2.jpg",
                            "offerId": 2429001,
                            "offerName": "alt_art_bundle",
                            "priority": 1,
                            "thumbnail": "https://d3t4xohaeg8xj9.cloudfront.net/kards/store/offer/offer_1_core_pack/core_packs_1_lowres2.jpg",
                            "title": "异画合集"
                        }
                    ],
                    "startDate": "2023-05-06T00:00:00Z"
                }
            ],
            "message": "Offers for 2025-08-23T04:20:09.024285",
            "status": 200,
            "ts": 1755922809.024285
        }
        resp.state = falcon.HTTP_200
