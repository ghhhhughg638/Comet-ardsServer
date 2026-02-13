import falcon
import falcon.asgi


class FPResource:
    async def on_get(self, req, resp):
        resp.media = {
            "changed": True,
            "elements": [
                {
                    "content": {
                        "banner_text": {
                            "font_size": 56,
                            "text": ""
                        },
                        "heading": {
                            "font_size": 80,
                            "text": "打开"
                        },
                        "icon": {
                            "icon_url": "https://helsinki-test.s3.eu-west-1.amazonaws.com/box-3/box_packs_icon.png"
                        },
                        "image_url": "https://helsinki-test.s3.eu-west-1.amazonaws.com/box-3/box_packs_edge.jpg",
                        "link": "kards:openpacks",
                        "priority": 1,
                        "slot": 2,
                        "sub_heading": {
                            "font_size": 80,
                            "text": "卡包"
                        },
                        "type": 1
                    },
                    "elementId": 27,
                    "endDate": "9999-12-31T23:59:00Z",
                    "isPublished": True,
                    "isTargeted": False,
                    "startDate": "0001-01-01T00:00:00Z"
                },
                {
                    "content": {
                        "banner_text": {
                            "font_size": 56,
                            "text": ""
                        },
                        "heading": {
                            "font_size": 80,
                            "text": "玩我！"
                        },
                        "icon": {
                            "icon_url": "https://helsinki-test.s3.eu-west-1.amazonaws.com/box-2/box_draft_icon.png"
                        },
                        "image_url": "https://helsinki-test.s3.eu-west-1.amazonaws.com/box-2/box_draft_edge_unclesam.jpg",
                        "link": "kards:draft",
                        "priority": 3,
                        "slot": 1,
                        "sub_heading": {
                            "font_size": 80
                        },
                        "type": 1
                    },
                    "elementId": 31,
                    "endDate": "2026-12-31T10:59:00Z",
                    "isPublished": True,
                    "isTargeted": False,
                    "startDate": "2024-06-24T08:00:00Z"
                },
                {
                    "content": {
                        "banner_text": {
                            "font_size": 56,
                            "text": ""
                        },
                        "heading": {
                            "font_size": 64,
                            "text": "Wards"
                        },
                        "icon": {
                            "icon_url": ""
                        },
                        "image_url": "http://103.91.208.25:5231/images/u",
                        "link": "",
                        "priority": 4,
                        "sub_heading": {
                            "font_size": 40,
                            "text": "元旦佳节，玩Wards 时候也别忘了给爱的人送上祝福哦！"
                        },
                        "type": 0
                    },
                    "elementId": 1,
                    "endDate": "2026-01-31T15:00:00Z",
                    "isPublished": True,
                    "isTargeted": False,
                    "startDate": "2023-11-06T11:00:00Z"
                },
                {
                    "content": {
                        "banner_text": {
                            "font_size": 56,
                            "text": ""
                        },
                        "heading": {
                            "font_size": 80,
                            "text": "QQ群"
                        },
                        "icon": {
                            "icon_url": "https://helsinki-test.s3.eu-west-1.amazonaws.com/box-1/BiliBili.png"
                        },
                        "image_url": "https://helsinki-test.s3.eu-west-1.amazonaws.com/box-1/box_discord_edge.jpg",
                        "link": "https://qm.qq.com/q/brJ40NkBIQ",
                        "priority": 2,
                        "slot": 0,
                        "sub_heading": {
                            "font_size": 56
                        },
                        "type": 1
                    },
                    "elementId": 35,
                    "endDate": "2025-12-31T15:00:00Z",
                    "isPublished": True,
                    "isTargeted": False,
                    "startDate": "2023-12-11T12:00:00Z"
                }
            ],
            "message": "OK",
            "status_code": 200,
            "targeted": []
        }
        resp.state = falcon.HTTP_200
