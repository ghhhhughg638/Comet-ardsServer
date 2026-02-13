import falcon
import falcon.asgi

from resources import *
from jwt_middleware import JWTAuthMiddleware
from config import JWT_KEY

jwt_middleware_a = JWTAuthMiddleware(secret_key=JWT_KEY)
app = falcon.asgi.App(middleware=jwt_middleware_a)

app.add_route('/.com/config', ConfigResource())
app.add_route('/', RootResource())
app.add_route('/session', SessionResource())
app.add_route('/items/{player_id}', ItemResource())
app.add_route('/players/{player_id}/librarynew', LibraryNewResource())
app.add_route('/matches/v2/', MatchesV2Resource())
app.add_route('/matches/v2/reconnect', ReConnectResource())
app.add_route('/players/{player_id}', PlayersResource())
app.add_route('/players/{player_id}/heartbeat', HeartBeatResource())
app.add_route('/players/{player_id}/packs', PacksResource())
app.add_route('/players/{player_id}/friends', FriendResource())
app.add_route('/fp/', FPResource())
app.add_route('/store/v2/', XsollaResource())
app.add_route('/lobbyplayers', LobbyplayersResource())
app.add_route('/players/{player_id}/decks', DecksResources())
app.add_route('/players/{player_id}/decks/{deck_id}', DeckUpdataResources())
