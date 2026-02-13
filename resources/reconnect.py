import falcon
import falcon.asgi


class ReConnectResource:
    async def on_get(self, req, resp):
        resp.media = 'running'
        resp.status = falcon.HTTP_200
