import falcon
import falcon.asgi


class HeartBeatResource:
    async def on_put(self, req, resp, player_id):
        resp.media = {}
        resp.status = falcon.HTTP_200
