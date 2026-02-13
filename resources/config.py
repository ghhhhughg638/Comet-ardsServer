from datetime import datetime


class ConfigResource:
    async def on_get(self, req, resp):
        resp.media = {
            "xserver_closed": "The servers will be up again at 10:00 UTC.\n\n服务器维护\n世界标准时间10:00(UTC)上线",
            "xserver_closed_header": "Server maintenance",
            "forgot_password_url": "https://www.kards.com/auth/recovery?lang={lang}"
        }