import falcon
from falcon import HTTPUnauthorized, Request, Response

from database import db, User
from websocket import server


class LobbyplayersResource:
    async def on_post(self, req: Request, resp: Response):
        try:
            credentials = await req.get_media()
            player_id = credentials.get('player_id')
            deck_id = credentials.get('deck_id')
            user: User = req.context.user
            if user.id == player_id and await db.Check_Deck_Presence(
                    id=deck_id) and user.id in server.id_to_websocket:
                if await server.add_match_players(conn_id=player_id, deck_id=deck_id):
                    resp.media = 'OK'
                else:
                    if player_id in server.waiting_queue:
                        resp.media = 'OK'
                        return
                    resp.status = falcon.HTTP_402
                    raise HTTPUnauthorized(description="Warning")
                print('hello')
                return
            else:
                resp.status = falcon.HTTP_400
                raise HTTPUnauthorized(description="Warning")
        except Exception as e:
            print(e)
