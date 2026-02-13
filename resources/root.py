from datetime import datetime, timezone

import jwt
from falcon import HTTPUnauthorized

from config import host, IP, version, JWT_KEY, JWT_algorithm
from database import db


class RootResource:
    async def on_get(self, req, resp):
        try:
            current_time = datetime.now(timezone.utc)
            server_time_z = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
            server_time_z = server_time_z

            endpoints = {
                "draft": f"http://{IP}/draft/",
                "email": f"http://{IP}/email/set",
                "lobbyplayers": f"http://{IP}/lobbyplayers",
                "matches": f"http://{IP}/matches",
                "matches2": f"http://{IP}/matches/v2/",
                "my_draft": None,
                "my_items": None,
                "my_player": None,
                "players": f"http://{IP}/players",
                "purchase": f"http://{IP}/store/v2/txn",
                "root": f"http://{IP}",
                "session": f"http://{IP}/session",
                "store": f"http://{IP}/store/",
                "tourneys": f"http://{IP}/tourney/",
                "transactions": f"http://{IP}/store/txn",
                "view_offers": f"http://{IP}/store/v2/"
            }

            build_info = {
                "build_timestamp": "2025-10-13T17:31:40Z",
                "commit_hash": "dfaf581c",
                "version": version
            }

            host_info = {
                "container_name": "kards-backend-LIVE",
                "docker_image": "618005890699.dkr.ecr.eu-west-1.amazonaws.com/kards-backend:live",
                "host_address": host,
                "host_name": "cometkards",
                "instance_id": "i-03598bff8bd68fdee"
            }

            auth_header = req.get_header('Authorization')
            if auth_header is None:
                current_user = {}
            else:
                token = auth_header.replace("JWT ", "")
                payload_client = jwt.decode(
                    token,
                    JWT_KEY,
                    algorithms=[JWT_algorithm]
                )
                user_id: str = payload_client.get("user_id")
                user = await db.Find_user_data(list_name="id", data=user_id)
                payload_server = jwt.decode(
                    user.player_JWT,
                    JWT_KEY,
                    algorithms=[JWT_algorithm]
                )
                if abs(payload_client.get("exp") - payload_server.get("exp")) < 86400:
                    pass
                else:
                    raise HTTPUnauthorized(description="Warning")
                endpoints['my_draft'] = f"http://{IP}/draft/{user_id}"
                endpoints['my_items'] = f"http://{IP}/items/{user_id}"
                endpoints['my_player'] = f"http://{IP}/players/{user_id}"
                current_user = {
                    "client_id": user_id,
                    "exp": user_id,
                    "external_id": user.username,
                    "iat": payload_server.get("exp"),
                    "identity_id": user_id,
                    "iss": "cometkards",
                    "jti": "",
                    "language": "zh-Hans",
                    "payment": "notavailable",
                    "player_id": user_id,
                    "provider": "device",
                    "roles": [],
                    "tier": "LIVE",
                    "user_id": user_id,
                    "user_name": user.username
                }
            root_data = {
                "build_info": build_info,
                "current_user": current_user,
                "endpoints": endpoints,
                "host_info": host_info,
                "server_time": server_time_z,
                "service_name": "kards-backend",
                "tenant_name": "1939-kardslive",
                "tier_name": "LIVE"
            }
            resp.media = root_data
        except Exception as e:
            print(e)