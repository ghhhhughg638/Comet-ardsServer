import jwt
from falcon import HTTPUnauthorized

from config import JWT_algorithm
from database import db


class JWTAuthMiddleware:
    def __init__(self, secret_key: str, algorithm: str = JWT_algorithm):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.excluded_prefixes = {
            "/items/",
        }
        self.excluded_paths = {
            "/.com/config",
            "/session",
            "/",
            #"/matches/v2/reconnect"

        }

    async def process_request(self, req, resp):
        try:
            for prefix in self.excluded_prefixes:
                if req.path.startswith(prefix):
                    return  # 跳过认证
            if req.path in self.excluded_paths:
                return

            auth_header = req.get_header("Authorization")
            if auth_header is None:
                raise HTTPUnauthorized(description="Warning")
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
                raise HTTPUnauthorized(description="Warning")

            req.context.user = user
        except Exception as e:
            print(e)
            raise HTTPUnauthorized(description="Warning")
